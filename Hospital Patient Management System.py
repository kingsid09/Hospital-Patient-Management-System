# Hospital Patient Management System


class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
        self.status = "Admitted"

    def __str__(self):
        return (
            f"Patient Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Disease : {self.disease}\n"
            f"Status : {self.status}\n"
        )


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = {}
        print(f"\n🏥 Welcome to {self.hospital_name}")
        print("Hospital System Started Successfully\n")

    def admit_patient(self, patient_id, patient):
        try:
            if not isinstance(patient, Patient):
                raise TypeError
            self.patients[patient_id] = patient
            print(f"Patient admitted with ID : {patient_id}\n")
        except TypeError:
            print("Error: Invalid patient data")

    def discharge_patient(self, patient_id):
        try:
            self.patients[patient_id].status = "Discharged"
            print("Patient discharged successfully\n")
        except KeyError:
            print("Error: Patient ID not found\n")

    def update_disease(self, patient_id, new_disease):
        try:
            self.patients[patient_id].disease = new_disease
            print("Disease updated successfully\n")
        except KeyError:
            print("Error: Patient ID not found\n")

    def view_patients(self):
        print("\n--------- Patient Records ---------")
        if not self.patients:
            print("No patients found.\n")
        else:
            for pid, patient in self.patients.items():
                print(f"Patient ID : {pid}")
                print(patient)
        print("----------------------------------\n")

    def search_patient(self, patient_id):
        if patient_id in self.patients:
            print("\nPatient Found:")
            print(self.patients[patient_id])
        else:
            print("Error: Patient not found\n")

    def remove_patient(self, patient_id):
        try:
            del self.patients[patient_id]
            print("Patient record removed successfully\n")
        except KeyError:
            print("Error: Patient not found\n")


# ---------------------- MENU ----------------------
hospital = Hospital("City Care Hospital")

while True:
    print("----- MENU -----")
    print("1. Admit Patient")
    print("2. Discharge Patient")
    print("3. Update Disease")
    print("4. View Patients")
    print("5. Search Patient")
    print("6. Remove Patient Record")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        try:
            age = int(input("Enter Age: "))
            disease = input("Enter Disease: ")
            hospital.admit_patient(pid, Patient(name, age, disease))
        except ValueError:
            print("Error: Age must be a number\n")

    elif choice == "2":
        pid = input("Enter Patient ID: ")
        hospital.discharge_patient(pid)

    elif choice == "3":
        pid = input("Enter Patient ID: ")
        disease = input("Enter New Disease: ")
        hospital.update_disease(pid, disease)

    elif choice == "4":
        hospital.view_patients()

    elif choice == "5":
        pid = input("Enter Patient ID: ")
        hospital.search_patient(pid)

    elif choice == "6":
        pid = input("Enter Patient ID: ")
        hospital.remove_patient(pid)

    elif choice == "7":
        print("Exiting Hospital System... Goodbye!")
        break

    else:
        print("Invalid choice, try again.\n")
