from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="Name of the Patient", description="Give the name of the patient in less than 50 characters", examples=['Vishesh','Madhav'])]
    email: EmailStr
    hospital_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the person Married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str,int]


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domain = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name', mode='before')
    @classmethod
    def transform_name(cls, value):
        return value.capitalize()
    

    @field_validator('age', mode='after')       # by  default mode is after   
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')


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


patient1_info = {"name":"vbp", "email":"vbp@hdfc.com", "hospital_url": "https://www.apollohospitals.com", "age":"22", "weight":65,  'contact_details':{'phone':789789}}


patient1 = Patient(**patient1_info)    # validation perfomerd here  --> type coercion

insert_patient_data(patient1)



