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
            print("ℹ️  INFO for {name}: {advice}")
        log_query(symptom, advice)
    else:
        print("Symptom not found. please consult a doctor.")

# a function to get translations from other languages.
def Translator(language):
    return Bemba_to_english.get(language, "sorry that word is not recognized.")

#A while loop to keep the process going
while True:
    checker = input("Enter your symptom: ").lower()
    if checker == "quit":
        print("You terminated the program, i hope you get better.")
        break
    elif checker in Symptoms:
        print_advice (name, checker)
    elif Translator(checker):
        english_symptom = Translator(checker)
        print(name, english_symptom)
    else:
        print("Symptom not recognized. please visit a clinic or Hospital")

