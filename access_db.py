from pymodm import connect


connect("mongodb+srv://maxinech:Mikan54669@bme547."
        "wdo8g.mongodb.net/health_db?retryWrites=true&w=majority")


def get_database_record():
    from database_info import Patient
    patient = Patient.objects.raw({"_id": 101}).first()
    print(patient.name)


def put_new_record():
    from database_info import Patient
    new_patient = Patient(name="David", patient_id=1)
    new_patient.save()


if __name__ == "__main__":
    put_new_record()
