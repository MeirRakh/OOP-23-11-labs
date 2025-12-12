class Doctor:
    def __init__(self, name, department, experience):
        self.name = name
        self.department = department
        self.experience = experience   # years
class Patient:
    def __init__(self, full_name, doctor):
        self.full_name = full_name
        self.doctor = doctor
class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
    def add_patient(self, patient):
        self.patients.append(patient)
    def show_patients(self):
        print(f"Patients in {self.name}:")
        for p in self.patients:
            print(f"- {p.full_name} (Doctor: {p.doctor.name}, "
                  f"Department: {p.doctor.department}, "
                  f"Experience: {p.doctor.experience} years)")
doctor = Doctor(
    input("Doctor name: "),
    input("Department: "),
    int(input("Experience (years): "))
)
patient = Patient("John Smith", doctor)
hospital = Hospital("Central Hospital")
hospital.add_patient(patient)
hospital.show_patients()
