name = input("May i know your name?: ")
Symptoms = {'fever': 'could be malaria,flu, or typhoid',
            'headache': 'could be dehydration, malaria, or, migraine',
            'cough': 'could be flu, pneumonia, or asthma',
            'diarrhea': 'could be food poisoning, cholera, or stomach infection',
            'chest pain': 'could be heart disease, pneumonia, or muscle strain',
            'rash': 'could be allergy, measles, or skin infection',
            'fatigue': 'could be anemia, depression, or chronic illness',
            'vomiting': 'could be food poisoning, pregnancy, or stomach flu',
            'sore throat': 'could be tonsillitis, flu, or strep throat',
            'eye pain': 'could be conjunctivitis, migraine, or eye strain'
            }

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
def symptom_checker(symptom):
    return Symptoms.get(symptom, "Symptom not found. please consult a doctor.")

def Translator(language):
    return Bemba_to_english.get(language, "sorry that word is not recognized.")

while True:
    checker = input("Enter your symptom: ").lower()
    if checker == "quit":
        print("You terminated the program, i hope you get better.")
        break
    elif checker in Symptoms:
        print (f"Here is a review for {name}; it {symptom_checker(checker)}")
    elif Translator(checker):
        english_symptom = Translator(checker)
        print(f"Here is a review for {name}; it {symptom_checker(english_symptom)}")
    else:
        print("Symptom not recognized. please visit a clinic or Hospital")
