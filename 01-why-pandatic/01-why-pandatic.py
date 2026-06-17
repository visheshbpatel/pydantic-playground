def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:

        if age<0:
            raise ValueError("Age can't be negative")
        
        print(name)
        print(age)
        print("Inserted into database")  # just for testing
    else:
        raise TypeError("Incorrect Datatype")
    

def update_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Updated into database")
    else:
        raise TypeError("Incorrect Datatype")



insert_patient_data("vbp", 8)

