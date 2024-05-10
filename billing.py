class Patient:
    def __init__(self, name, dob, address, phone):
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.medical_records = []

class MedicalRecord:
    def __init__(self, date, doctor, diagnosis, medication):
        self.date = date
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.medication = medication

class MedicalHistorySystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, dob, address, phone):
        patient = Patient(name, dob, address, phone)
        self.patients.append(patient)
        return patient

    def add_medical_record(self, patient, date, doctor, diagnosis, medication):
        record = MedicalRecord(date, doctor, diagnosis, medication)
        patient.medical_records.append(record)
        return record

    def search_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

# Example Usage
system = MedicalHistorySystem()
patient1 = system.add_patient("John Doe", "1990-01-01", "123 Main St", "555-1234")
record1 = system.add_medical_record(patient1, "2024-05-10", "Dr. Smith", "Headache", "Tylenol")

# Search for a patient
patient = system.search_patient("John Doe")
if patient:
    for record in patient.medical_records:
        print("Date:", record.date)
        print("Doctor:", record.doctor)
        print("Diagnosis:", record.diagnosis)
        print("Medication:", record.medication)
else:
    print("Patient not found.")
