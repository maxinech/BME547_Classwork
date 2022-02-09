class Patient:

    def __init__(self, patient_name, patient_id, age, dob=None):
        self.name = patient_name
        self.id = patient_id
        self.age = age
        self.tests = []
        self.dob = dob

    def __repr__(self):
        return "Patient: {},{}".format(self.name, self.id)

    def output_patient(self):
        outstring = "Name: {}\n".format(self.name)
        outstring += "Id: {}\n".format(self.id)
        outstring += "Age: {}\n".format(self.age)
        outstring += "Tests: {}\n".format(self.tests)
        return outstring

    def is_adult_or_minor(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Minor"

    def id_tag_string(self):
        return "{}: {}".format(self.name, self.id)

    def add_test(self, test_name, test_result):
        self.tests.append((test_name, test_result))

    def increase_age(self, number_of_years):
        self.age += number_of_years


def add_patient(patient_name, patient_id, age, dob=None):
    new_patient = Patient(patient_name, patient_id, age, dob)
    return new_patient


def main():
    db = []
    x = add_patient("Ann Ables", 342, 40)
    db.append(x)
    # print(db[0].name)
    y = add_patient("Bob Boyles", 50, 50, "1/1/2000")
    db.append(y)
    z = add_patient("Chris Columbus", 111, 35)
    db.append(z)
    db.append(add_patient("David Dinkins", 22, 72))
    print(db)
    found_patient = find_patient(db, 111)
    print(found_patient.id_tag_string())
    print(found_patient.output_patient())
    # output_database(db)
    add_test_to_patient(db, 111, "HDL", 100)
    # output_database(db)
    return db


def output_database(db):
    for patient in db:
        output_patient(patient)


def output_patient(patient):
    for key in patient:
        print("{}: {}".format(key, patient[key]))
    # x = "physician"
    # if x in patient:
    #     do something
    # else:
    #     report no physician


def find_patient(db, id_no):
    for patient in db:
        if patient.id == id_no:
            return patient
    return


def add_test_to_patient(db, id_no, test_name, test_result):
    patient = find_patient(db, id_no)
    test_tuple = (test_name, test_result)
    patient.tests.append(test_tuple)


def print_directory(db):
    rooms = ["Room 13", "Room 12", "Room 99", "Room 3"]
    for room, patient in zip(rooms, db):
        print("{} - {}".format(patient.name, room))

        # print("Name: {}  Room: {}".format(patient[0], rooms[i]))


def create_id_tag_string(patient):
    id_string = "{}: {}".format(patient["name"], patient["id"])
    return id_string


if __name__ == "__main__":
    db = main()
    print_directory(db)
    # print(create_id_tag_string(find_patient(db, 111)))
