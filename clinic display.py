import json
#Load clinics.json
try:
    with open("c:\\Users\\Vexy Technology\\Desktop\\Bantu AI\\Symptom_checker\\flask\\clinics.json", "r") as file:
        clinics = json.load(file)
#Print each clinic
    for clinic in clinics:
        print(f"{clinic['name']} ({clinic['district']}) - phone: {clinic['phone']}, NHIMA: {clinic['nhima_accepted']}, Hours: {clinic['hours']}")
except FileNotFoundError:
    print("File not found.")
clinics = []