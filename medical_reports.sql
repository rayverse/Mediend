USE medical_reports;
DROP TABLE reports;
CREATE TABLE reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report TEXT NOT NULL,
    label TEXT NOT NULL
);
INSERT INTO reports (report, label) VALUES
('Patient presents with persistent cough, fever, and fatigue for past 2 weeks.', 'Respiratory Infection'),
('Regular checkup shows elevated blood pressure and irregular heartbeat.', 'Cardiovascular Disease'),
('Complaint of joint pain and morning stiffness in multiple joints.', 'Rheumatoid Arthritis'),
("Severe coughing fits, especially at night, with thick mucus production.", "Respiratory Infection"),
("Upper respiratory symptoms including congestion and productive cough.", "Respiratory Infection"),
("Patient reports fever of 101.2F, sore throat, and persistent cough.", "Respiratory Infection"),
("Symptoms include difficulty breathing, wheezing, and chest congestion.", "Respiratory Infection"),
("Patient presents with flu-like symptoms, including fever and body aches.", "Respiratory Infection"),
("Chronic cough with yellow sputum production and nasal congestion.", "Respiratory Infection");

INSERT INTO reports (report, label) VALUES
("Regular checkup shows elevated blood pressure and irregular heartbeat.", "Cardiovascular Disease"),
("Patient reports chest pain, shortness of breath, and palpitations.", "Cardiovascular Disease"),
("Cardiovascular examination reveals murmur and elevated BP readings.", "Cardiovascular Disease"),
("History of hypertension, now presenting with chest discomfort.", "Cardiovascular Disease"),
("Patient experiencing dizziness with elevated blood pressure readings.", "Cardiovascular Disease"),
("ECG shows irregular rhythm, patient reports occasional chest tightness.", "Cardiovascular Disease"),
("History of cardiac issues with new onset of exercise intolerance.", "Cardiovascular Disease"),
("Patient presents with chest pain radiating to the left arm, shortness of breath, and dizziness.", "Cardiovascular Disease"),
("Acute onset of crushing chest pain, sweating, and nausea.", "Cardiovascular Disease");
INSERT INTO reports (report, label) VALUES 
("Complaint of joint pain and morning stiffness in multiple joints.", "Rheumatoid Arthritis"),
("Severe inflammation in fingers and wrists, difficulty with fine motor tasks.", "Rheumatoid Arthritis"),
("Progressive joint pain affecting multiple joints, worse in the morning.", "Rheumatoid Arthritis"),
("Bilateral hand pain with visible joint swelling and reduced grip strength.", "Rheumatoid Arthritis"),
("Patient reports symmetric joint pain and morning stiffness lasting >1 hour.", "Rheumatoid Arthritis"),
("Multiple joint inflammation with characteristic rheumatoid nodules.", "Rheumatoid Arthritis"),
("Chronic joint pain with associated swelling and reduced range of motion.", "Rheumatoid Arthritis");
INSERT INTO reports (report, label) VALUES 
("Patient reports increased thirst, frequent urination, and fatigue.", "Diabetes"),
("History of obesity, now presenting with elevated blood glucose levels.", "Diabetes"),
("Symptoms include blurred vision, slow-healing wounds, and weight loss.", "Diabetes"),
("Patient with family history of diabetes, now showing signs of hyperglycemia.", "Diabetes");
INSERT INTO reports (report, label) VALUES 
("Patient complains of abdominal pain, bloating, and irregular bowel movements.", "Gastrointestinal Disorder"),
("History of GERD, now presenting with heartburn and regurgitation.", "Gastrointestinal Disorder"),
("Symptoms include nausea, vomiting, and epigastric pain.", "Gastrointestinal Disorder"),
("Patient reports chronic diarrhea and weight loss.", "Gastrointestinal Disorder");
INSERT INTO reports (report, label) VALUES 
("Patient reports persistent sadness, loss of interest, and insomnia.", "Mental Health Condition"),
("History of anxiety, now presenting with panic attacks and restlessness.", "Mental Health Condition"),
("Symptoms include mood swings, irritability, and difficulty concentrating.", "Mental Health Condition"),
("Patient with family history of depression, now showing signs of low mood.", "Mental Health Condition");  
INSERT INTO reports (report, label) VALUES 
("Patient presents with fatigue, joint pain, and a butterfly rash on the face.", "Autoimmune Disorder"),
("Complaint of dry eyes, dry mouth, and difficulty swallowing dry foods.", "Autoimmune Disorder");
INSERT INTO reports (report, label) VALUES 
("Tall stature, long limbs, and chest pain with a family history of aortic dissection.", "Rare Genetic Condition"),
("Chronic cough, poor weight gain, and salty-tasting skin in a 10-year-old boy.", "Rare Genetic Condition");
INSERT INTO reports (report, label) VALUES 
("High fever, confusion, and diarrhea in a patient with recent travel history.", "Unusual Presentation of Common Disease"),
("Fatigue, shortness of breath, and mild chest discomfort in a diabetic patient.", "Unusual Presentation of Common Disease");
INSERT INTO reports (report, label) VALUES 
("Shortness of breath, skin rash, and joint pain in a 40-year-old female.", "Complex Multi-System Disorder"),
("Skin thickening, difficulty swallowing, and Raynaud’s phenomenon in a 55-year-old female.", "Complex Multi-System Disorder");
INSERT INTO reports (report, label) VALUES 
("Fever, rash, and conjunctivitis in a patient with recent travel to South America.", "Emerging or Unusual Infection"),
("Fever, shortness of breath, and myalgia in a patient with rodent exposure.", "Emerging or Unusual Infection");
INSERT INTO reports (report, label) VALUES 
("Headache, confusion, and seizures in a 60-year-old male with a frontal lobe mass.", "Rare Cancer"),
("Episodic headaches, sweating, and palpitations in a 45-year-old female with hypertension.", "Rare Cancer");
INSERT INTO reports (report, label) VALUES 
("Progressive memory loss, confusion, and behavioral changes in a 70-year-old male.", "Neurological Disorder"),
("Tremors, rigidity, and bradykinesia in a 65-year-old male.", "Neurological Disorder");
INSERT INTO reports (report, label) VALUES 
("Fatigue, weight gain, and cold intolerance in a 50-year-old female.", "Metabolic Disorder"),
("Episodes of hypoglycemia, sweating, and confusion in a 30-year-old male.", "Metabolic Disorder");
INSERT INTO reports (report, label) VALUES 
("Chest pain, shortness of breath, and elevated troponin in a 25-year-old female.", "Rare Cardiovascular Condition"),
("Syncope, palpitations, and family history of sudden cardiac death in a 20-year-old male.", "Rare Cardiovascular Condition");
INSERT INTO reports (report, label) VALUES 
("Failure to thrive, developmental delay, and seizures in a 2-year-old child.", "Uncommon Pediatric Condition"),
("Recurrent infections, bruising, and fatigue in a 5-year-old child.", "Uncommon Pediatric Condition");

SELECT * FROM reports;


