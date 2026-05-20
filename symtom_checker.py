print("===AI Symptom checker===")
print("Good day, how are you today?")
print("please feel free to tell me whats wrong, i'm all ears")
symptom_1=input("please enter Symptom 1: ")
symptom_2=input("please enter Symptom 2: ")
symptom_3=input("please enter Symptom 3: ")
if symptom_1 == "fever" and symptom_2 == "headache":
    print("please visit the clinic and stay hydrated,you likely have malaria")
    print("the risk level is high")
elif symptom_1 == "cough" and symptom_2 == "sore throat":
    print("it is likely a common cough")
    print("take some rest and drink fluids")
    print("the risk level is low")
else:
    print("Symptoms not recognized please consult a doctor")