#importing date and time.

import datetime
# function to store advice and symptoms in query_log
def log_query(symptom, advice):
    with open("query_log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} | {symptom} | {advice}\n")

name = input("May i know your name?: ")

#A dictionary that holds the symptoms and replies needed
Symptoms = {'fever': {'advice': 'could be malaria, flu, or typhoid', 'severity': 'medium'},
            'headache': {'advice': 'could be dehydration, malaria, or, migraine', 'severity': 'low'},
            'cough': {'advice': 'could be flu, pneumonia, or asthma', 'severity': 'low'},
            'diarrhea': {'advice': 'could be food poisoning, cholera, or stomach infection', 'severity': 'high'},
            'chest pain': {'advice': 'could be heart disease, pneumonia, or muscle strain', 'severity': 'medium'},
            'rash': {'advice': 'could be allergy, measles, or skin infection', 'severity': 'low'},
            'fatigue': {'advice': 'could be anemia, depression, or chronic illness', 'severity': 'low'},
            'vomiting': {'advice': 'could be food poisoning, pregnancy, or stomach flu', 'severity': 'medium'},
            'sore throat': {'advice': 'could be tonsillitis, flu, or strep throat', 'severity': 'high'},
            'eye pain': {'advice': 'could be conjunctivitis, migraine, or eye strain', 'severity': 'medium'},
            'shortness of breath': {'advice': 'could be asthma,pneumonia, or heart failure', 'severity': 'high'},
            'dizziness': {'advice': 'could be low blood pressure, anemia, or vertigo', 'severity': 'medium'},
            'nausea': {'advice': 'could be food poisoning, pregnancy, or stomach flu', 'severity':'medium'},
            'back pain': {'advice': 'could be muscle strain, arthritis, or kidney infection', 'severity': 'medium'},
            'joint pain': {'advice': 'could be arthritis, lupus, or injury', 'severity': 'medium'},
            'abdominal': {'advice': 'could be appendicitis, ulcer, or indigestion', 'severity': 'high'},
            'swelling': {'advice': 'could be infection, kidney disease, or heart  failure', 'severity': 'high'},
            'weight loss': {'advice': 'could be diabetes, cancer, or thyroid disorder', 'severity': 'high'},
            'weight gain': {'advice': 'could be thyroid disorder, fluid retention, or overeating', 'severity': 'medium'},
            'night sweats': {'advice': 'could be tuberculosis, lymphoma, or menopause', 'severity': 'high'},
            'loss of appetite': {'advice': 'could be depression, infection, or cancer', 'severity': 'medium'},
            'memory loss': {'advice': 'could be dementia, stroke, or vitamin deficiency', 'severity': 'high'},
            'difficulty sleeping': {'advice': 'could be insomnia, stress, or sleep apnea', 'severity': 'medium'},
            'frequent urination': {'advice': 'could be diabetes, UTI, or prostate issues', 'severity': 'medium'},
            'burning urination': {'advice': 'could be UTI, STI, or bladder infection', 'severity': 'high'},
            'bloody stool': {'advice': 'could be hemorrhoids, ulcer, or colon cancer', 'severity': 'high'},
            'bloody urine': {'advice': 'could be kidney stones, infection, or thyroid disorder', 'severity': 'high'},
            'palpitations': {'advice': 'could be arrhythmia, anxiety, or thyroid disorder', 'severity': 'high'},
            'swollen lymph nodes': {'advice': 'could be infection, lymphoma, or cancer', 'severity': 'high'},
            'hearing loss': {'advice': 'could be ear infection, aging, or loud exposure', 'severity': 'medium'},
            'blurred vision': {'advice': 'could be diabetes, cataracts, or eye strain', 'severity': 'medium'},
            'sensitivity to light': {'advice': 'could be migraine. meningitis,  or eye infection', 'severity': 'low'},
            'skin dryness': {'advice': 'could be eczema, dehydration, or thyroid disorder', 'severity': 'low'},
            'itching': {'advice': 'could be allergy, eczema, or liver disease', 'severity': 'medium'},
            'swollen ankles': {'advice': 'could be heart failure, kidney disease, or pregnancy', 'severity': 'high'},
            'difficulty swallowing': {'advice': 'could be throat infection, stroke, or esophageal cancer', 'severity': 'high'},
            'hoarseness': {'advice': 'could be laryngitis, vocal strain, or thyroid disorder', 'severity': 'medium'},
            'tremors': {'advice': 'could be parkinson disease, anxiety, or thyroid disorder', 'severity': 'high'},
            'numbness': {'advice': 'could be stroke, nerve damage, or multiple sclerosis', 'severity': 'high'},
            'cold hands and feet': {'advice': 'could be poor circulation, anemia, or diabetes', 'severity': 'medium'}
            }

#A dictionary that holds Bemba phrases that are used to interact with the system using different languages
Bemba_to_english = {
    'nde unfwa umubili nau kaba': 'fever',
    'nde unfwa umutwe ule kalipa': 'headache',
    'nin jamba uku kola sana': 'cough',
    'nindwala shiki': 'diarrhea',
    'chifuba chule kalipa': 'chest pains',
    'ninkwata impele': 'rash',
    'ndeufwa ukunaka': 'fatigue',
    'nde luka sana': 'vomiting',
    'ukukalipa pa mukoshi': 'sore throat',
    'ukukalipa kwa menso': 'eye pain'
}

#Clinic/Hospital Recommendation.
nearest_clinic_map = {
    "chilenje": "chilenje Clinic",
    "matero": "Matero Main Clinic",
    "kanyama": "Kanyama Clinic",
    "woodlands": "Woodlands Clinic",
    "chelstone": "Chelstone Clinic"
}

#a function to print the nearest clinic
def get_nearest_clinic(district):
    return nearest_clinic_map.get(district.lower(), "District not recognized. please visit the nearest hospital.")

#A function to get symptoms and advice
def symptom_checker(symptom):
    entry = Symptoms.get(symptom)
    if entry:
        return entry["advice"], entry["severity"]
    else:
        return None, None

# a function to print the requests made by the user
def print_advice(name, symptom):
    advice, severity =symptom_checker(symptom)
    if advice:
        if severity == "high":
            print(f"⚠️  URGENT for {name}: {advice}")
        elif severity == "medium":
            print(f"⚠️  CAUTION for {name}: {advice}")
        else:
            print(f"ℹ️  INFO for {name}: {advice}")
        log_query(symptom, advice)
    else:
        print("Symptom not found. please consult a doctor.")

# a function to get translations from other languages.
def Translator(language):
    return Bemba_to_english.get(language, "sorry that word is not recognized please visit a Clinic.")

# adding query logging
def read_log():
    try:
        with open("query_log.txt", "r") as f:
            print("\n--- Query History ---")
            for line in f:
                print(line.strip())
            print("------------------------------------\n")
    except FileNotFoundError:
        print("No queries logged yet.")

# a function to print all symptoms.
def show_symptoms():
    print("\n----------------------------- List of Symptoms -------------------------------------------------")
    for symptom, details in Symptoms.items():
        print(f"{symptom.title()} (severity: {details['severity']}) → {details['advice']}")
    print("------------------------------------------------------------------------------------------------\n")

#A while loop to keep the process going
while True:
    checker = input("Enter your symptom: ").lower()
    if checker == "quit":
        print("You terminated the program, i hope you get better.")
        read_log() #it shows the history before exiting.
        break
    elif checker == "help":
        show_symptoms()
    elif checker in Symptoms:
        print_advice (name, checker)
        district = input("Enter your district (Chilenje, Matero, Kanyama, Woodlands, Chelstone): ")
        print(f"Nearest clinic: {get_nearest_clinic(district)}")
    elif Translator(checker):
        english_symptom = Translator(checker)
        print(name, english_symptom)
        district = input("Enter your district (Chilenje, Matero, Kanyama, Woodlands, Chelstone): ")
        print(f"Nearest clinic: {get_nearest_clinic(district)}")
    elif checker == "help":
        print(f"{Symptoms}\n", f"{Bemba_to_english}" )
    else:
        print("Symptom not recognized. please visit a clinic or Hospital")

