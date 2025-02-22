import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate, StratifiedKFold  # Add StratifiedKFold here
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, make_scorer, precision_score, recall_score, f1_score, accuracy_score
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Initialize NLTK components
import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# MySQL database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'Tick134Tack365',  # Replace with your MySQL password
    'database': 'medical_reports'
}

def initialize_database():
    """Initialize the MySQL database and create tables if they don't exist."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            report TEXT NOT NULL,
            label TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_report_to_db(report, label):
    """Save a new report and its label to the database."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reports (report, label) VALUES (%s, %s)
    ''', (report, label))
    conn.commit()
    conn.close()

def load_reports_from_db():
    """Load all reports and labels from the database."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT report, label FROM reports')
    rows = cursor.fetchall()
    conn.close()
    
    reports = [row[0] for row in rows]
    labels = [row[1] for row in rows]
    return reports, labels

class MedicalReportAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.classifier = RandomForestClassifier(
            n_estimators=100,
            min_samples_leaf=2,
            random_state=42
        )
        self.label_encoder = LabelEncoder()
        
    def preprocess_text(self, text):
        """Clean and preprocess medical report text."""
        text = str(text).lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
        tokens = word_tokenize(text)
        tokens = [t for t in tokens if t not in self.stop_words and len(t) > 2]  # Remove stopwords and short tokens
        return ' '.join(tokens)
    
    def prepare_data(self, reports, labels):
        """Prepare data for training."""
        if len(reports) != len(labels):
            raise ValueError("Number of reports must match number of labels")
        
        processed_reports = [self.preprocess_text(report) for report in reports]
        X = self.vectorizer.fit_transform(processed_reports)
        y = self.label_encoder.fit_transform(labels)
        
        return X, y
    
    def evaluate_model(self, X, y):
        """Evaluate model using stratified cross-validation."""
        scoring = {
            'accuracy': make_scorer(accuracy_score),
            'precision_macro': make_scorer(precision_score, average='macro', zero_division=0),
            'recall_macro': make_scorer(recall_score, average='macro', zero_division=0),
            'f1_macro': make_scorer(f1_score, average='macro', zero_division=0)
        }
        
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        scores = cross_validate(
            self.classifier, X, y,
            scoring=scoring,
            cv=cv,
            return_train_score=True
        )
        
        return scores
    
    def train(self, reports, labels):
        """Train the model on medical reports."""
        try:
            X, y = self.prepare_data(reports, labels)
            scores = self.evaluate_model(X, y)
            self.classifier.fit(X, y)
            return scores
        except Exception as e:
            st.error(f"Error during training: {str(e)}")
            raise
    
    def analyze_report(self, report):
        """Analyze a new medical report."""
        try:
            processed_report = self.preprocess_text(report)
            X = self.vectorizer.transform([processed_report])
            probs = self.classifier.predict_proba(X)[0]
            
            results = []
            for idx in np.argsort(probs)[::-1]:
                condition = self.label_encoder.classes_[idx]
                probability = probs[idx]
                if probability > 0.1:  # Only include significant probabilities
                    results.append({
                        'condition': condition,
                        'probability': probability,
                        'risk_level': 'High' if probability > 0.7 else 
                                    'Medium' if probability > 0.4 else 'Low'
                    })
            
            return results
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
            raise

# Streamlit UI
def main():
    st.title("Medical Report Analyzer")
    st.write("Upload or enter a medical report to get an early diagnosis.")

    # Initialize database
    initialize_database()

    # Load reports from the database
    reports, labels = load_reports_from_db()

    # Initialize analyzer
    analyzer = MedicalReportAnalyzer()

    # Train the model on existing data
    if reports and labels:
        st.write("Training model on existing data...")
        scores = analyzer.train(reports, labels)
        st.write("Cross-validation Results:")
        st.write(f"Accuracy: {scores['test_accuracy'].mean():.3f} (+/- {scores['test_accuracy'].std() * 2:.3f})")
        st.write(f"Precision: {scores['test_precision_macro'].mean():.3f} (+/- {scores['test_precision_macro'].std() * 2:.3f})")
        st.write(f"Recall: {scores['test_recall_macro'].mean():.3f} (+/- {scores['test_recall_macro'].std() * 2:.3f})")
        st.write(f"F1-score: {scores['test_f1_macro'].mean():.3f} (+/- {scores['test_f1_macro'].std() * 2:.3f})")
    else:
        st.warning("No data found in the database. Please add reports to train the model.")

    # Input for new report
    st.header("Analyze a New Report")
    user_input = st.text_area("Enter a doctor's report:")

    if st.button("Analyze"):
        if user_input:
            results = analyzer.analyze_report(user_input)
            st.write("Analysis Results:")
            for result in results:
                st.write(f"**Condition:** {result['condition']}")
                st.write(f"**Probability:** {result['probability']:.2f}")
                st.write(f"**Risk Level:** {result['risk_level']}")
                st.write("---")
        else:
            st.warning("Please enter a valid report.")

    # Feedback and correction
    st.header("Feedback")
    feedback = st.radio("Was the prediction correct?", ("Yes", "No"))
    if feedback == "No":
        correct_condition = st.text_input("Please enter the correct condition:")
        if st.button("Submit Feedback"):
            save_report_to_db(user_input, correct_condition)
            st.success("Report saved. The model will be retrained with the updated data.")

if __name__ == "__main__":
    main()