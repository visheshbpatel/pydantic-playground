from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float  #kg
    height: float  #mtr
    married: bool  
    contact_details: Dict[str,int]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print("Inserted into database")  # just for testing


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print("BMI: ",patient.bmi)
    print("Update into database")  # just for testing


patient1_info = {"name":"vbp", "email":"vbp@hdfc.com", "age":"65", "weight":65, "height":1.72, "married":False,  'contact_details':{'phone':789789, 'emergency':898989}}


patient1 = Patient(**patient1_info)    # validation perfomerd here  --> type coercion

update_patient_data(patient1)



