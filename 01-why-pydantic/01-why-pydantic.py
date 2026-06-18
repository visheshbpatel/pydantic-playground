from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="Name of the Patient", description="Give the name of the patient in less than 50 characters", examples=['Vishesh','Madhav'])]
    email: EmailStr
    hospital_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[Optional[bool], Field(default=None, description="Is the person Married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str,str]


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.github_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into database")  # just for testing


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.github_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Update into database")  # just for testing


patient1_info = {"name":"vbp", "email":"vbp@gmail.com", "hospital_website": "https://www.apollohospitals.com", "age":22, "weight":65,  'contact_details':{'phone':"789789"}}
# married was not provided, so it defaults to None
# # allergies was not added because it is option and set as None

patient1 = Patient(**patient1_info)

insert_patient_data(patient1)

