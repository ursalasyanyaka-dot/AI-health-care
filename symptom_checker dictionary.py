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

def symptom_checker(symptom):
    return Symptoms.get(symptom, "Symptom not found. please consult a doctor.")

checker = input("Enter symptom: ")
print (symptom_checker(checker))