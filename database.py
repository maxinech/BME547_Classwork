def add_patient(patient_name, patient_id, age):
    new_patient = {"name": patient_name,
                   "id": patient_id,
                   "age": age,
                   "tests": []}
    return new_patient


def main():
    db = []
    x = add_patient("Ann Ables", 342, 40)
    db.append(x)
    y = add_patient("Bob Boyles", 50, 50)
    db.append(y)
    z = add_patient("Chris Columbus", 111, 35)
    db.append(z)
    db.append(add_patient("David Dinkins", 22, 72))
    found_patient = find_patient(db, 111)
    print(found_patient)
    output_database(db)
    add_test_to_patient(db, 111, "HDL", 100)
    output_database(db)
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
        if patient["id"] == id_no:
            return patient
    return


def add_test_to_patient(db, id_no, test_name, test_result):
    patient = find_patient(db, id_no)
    test_tuple = (test_name, test_result)
    patient["tests"].append(test_tuple)


def print_directory(db):
    rooms = ["Room 13", "Room 12", "Room 99", "Room 3"]
    for room, patient in zip(rooms, db):
        print("{} - {}".format(patient["name"], room))

        # print("Name: {}  Room: {}".format(patient[0], rooms[i]))


def create_id_tag_string(patient):
    id_string = "{}: {}".format(patient["name"], patient["id"])
    return id_string


if __name__ == "__main__":
    db = main()
    print_directory(db)
    print(create_id_tag_string(find_patient(db, 111)))
    print(db[2]["tests"][0][0])
