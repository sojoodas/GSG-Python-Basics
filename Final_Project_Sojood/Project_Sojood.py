import json

patients_file = "patients.json"

def load_data():
    try:
        with open(patients_file, "r") as f:
            patients = json.load(f)
            return patients
    except FileNotFoundError:
        print("No saved data found. Starting with an empty system.")
        return []

def save_data():
    with open(patients_file, "w") as f:
        json.dump(patients, f, indent=4)

    print("Data saved successfully.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))

            if age > 0:
                return age
            else:
                print("Invalid age. Please enter a number greater than 0.")

        except ValueError:
            print("Invalid age. Please enter a number.")

def get_valid_id(message):
    while True:
        try:
            patient_id = int(input(message))
            return patient_id

        except ValueError:
            print("Invalid ID. Please enter a number.")

def get_confirmation(message):
    while True:
        confirm = input(message).strip().lower()

        if confirm == "yes" or confirm == "no":
            return confirm
        else:
            print("Please enter yes or no.")

def get_symptoms():
    while True:
        symptoms_text = input("Enter symptoms separated by comma: ").strip()

        if symptoms_text == "":
            print("Symptoms cannot be empty.")
        else:
            symptoms_list = symptoms_text.split(",")

            symptoms = []

            for symptom in symptoms_list:
                symptom = symptom.strip()

                if symptom != "":
                    symptoms.append(symptom)

            return symptoms

def get_next_id():
    if len(patients) == 0:
        return 1

    highest_id = patients[0]["id"]

    for patient in patients:
        if patient["id"] > highest_id:
            highest_id = patient["id"]

    return highest_id + 1

def find_patient_by_id(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    return None

def print_patient(patient):
    print(f"ID: {patient['id']}")
    print(f"Name: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Phone: {patient['phone']}")

    print("Symptoms:")
    for symptom in patient["symptoms"]:
        print(f"- {symptom}")

    print(30 * "-")
    print()

def add_patient():
    patient_id = get_next_id()

    name = input("Enter patient name: ").strip().title()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter patient name: ").strip().title()

    age = get_valid_age()

    phone = input("Enter phone number: ").strip()

    while phone == "":
        print("Phone number cannot be empty.")
        phone = input("Enter phone number: ").strip()

    symptoms = get_symptoms()

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "phone": phone,
        "symptoms": symptoms,
        "visits": []
    }

    patients.append(patient)

    print("Patient added successfully.")
    print(f"Patient ID: {patient_id}")

def view_patients():
    if len(patients) == 0:
        print("No patients found.")
    else:
        print()
        print("====== All Patients ======")
        print()
        for patient in patients:
            print_patient(patient)

def search_patient():
    search_value = input("Enter patient name or ID: ").strip()

    if search_value == "":
        print("Search value cannot be empty.")
        return

    if search_value.isdigit():
        patient_id = int(search_value)
        patient = find_patient_by_id(patient_id)

        if patient is None:
            print("Patient not found.")
        else:
            print("Patient found:")
            print_patient(patient)

    else:
        matches = []

        for patient in patients:
            if search_value.lower() in patient["name"].lower():
                matches.append(patient)

        if len(matches) == 0:
            print("Patient not found.")

        elif len(matches) == 1:
            print("Patient found:")
            print_patient(matches[0])

        else:
            print("More than one patient found.")
            print("Please choose the correct patient ID from the list:")

            for patient in matches:
                print(f"ID: {patient['id']} - Name: {patient['name']}")

            patient_id = get_valid_id("Enter patient ID to view full details: ")
            patient = find_patient_by_id(patient_id)

            if patient is None:
                print("Patient not found.")
            else:
                print("Patient found:")
                print_patient(patient)

def update_patient():
    patient_id = get_valid_id("Enter patient ID to update: ")
    patient = find_patient_by_id(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    while True:
        print("What do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Phone")
        print("4. Symptoms")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            new_name = input("Enter new name: ").strip().title()

            if new_name == "":
                print("Name cannot be empty.")
            else:
                patient["name"] = new_name
                print("Patient updated successfully.")

        elif choice == "2":
            patient["age"] = get_valid_age()
            print("Patient updated successfully.")

        elif choice == "3":
            new_phone = input("Enter new phone number: ").strip()

            if new_phone == "":
                print("Phone number cannot be empty.")
            else:
                patient["phone"] = new_phone
                print("Patient updated successfully.")

        elif choice == "4":
            patient["symptoms"] = get_symptoms()
            print("Patient updated successfully.")

        elif choice == "5":
            print("Returning to main menu.")
            break

        else:
            print("Invalid choice.")

def add_visit_note():
    patient_id = get_valid_id("Enter patient ID: ")
    patient = find_patient_by_id(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    print("Patient found:")
    print_patient(patient)

    confirm = get_confirmation("Is this the correct patient? (yes/no): ")

    if confirm == "no":
        print("Visit note cancelled.")
        return

    visit_date = input("Enter visit date: ").strip()

    while visit_date == "":
        print("Visit date cannot be empty.")
        visit_date = input("Enter visit date: ").strip()

    doctor = input("Enter doctor name: ").strip().title()

    while doctor == "":
        print("Doctor name cannot be empty.")
        doctor = input("Enter doctor name: ").strip().title()

    note = input("Enter visit note: ").strip()

    while note == "":
        print("Visit note cannot be empty.")
        note = input("Enter visit note: ").strip()

    advice = input("Enter prescription/advice: ").strip()

    while advice == "":
        print("Prescription/advice cannot be empty.")
        advice = input("Enter prescription/advice: ").strip()

    visit = {
        "date": visit_date,
        "doctor": doctor,
        "note": note,
        "advice": advice
    }

    patient["visits"].append(visit)

    print("Visit note added successfully.")

def view_patient_history():
    patient_id = get_valid_id("Enter patient ID: ")
    patient = find_patient_by_id(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    print(f"Patient: {patient['name']}")

    if len(patient["visits"]) == 0:
        print("No visit history found.")
    else:
        visit_number = 1

        for visit in patient["visits"]:
            print(f"Visit {visit_number}:")
            print(f"Date: {visit['date']}")
            print(f"Doctor: {visit['doctor']}")
            print(f"Note: {visit['note']}")
            print(f"Advice: {visit['advice']}")
            print(20 * "-")

            visit_number += 1

def show_menu():
    print()
    print("====== Clinic Patient Management System ======")
    print("1. Add New Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient Information")
    print("5. Add Visit Note")
    print("6. View Patient History")
    print("7. Save Data")
    print("8. Exit")
    print()

def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            add_visit_note()

        elif choice == "6":
            view_patient_history()

        elif choice == "7":
            save_data()

        elif choice == "8":
            confirm = get_confirmation("Are you sure you want to exit? (yes/no): ")

            if confirm == "yes":
                save_data()
                print("Thank you for using the Clinic Patient Management System.")
                print("Goodbye!")
                break
            else:
                print("Returning to main menu.")

        else:
            print("Invalid choice.")

patients = load_data()

main()

# DONE_SOJOOD_ABUSAADA :)