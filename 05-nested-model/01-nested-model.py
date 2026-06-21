from pydantic import BaseModel

class Address(BaseModel):
    
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address


address_dict = {"city": 'indore', "state":'madhya pradesh', "pin":'454545'}

address1 = Address(**address_dict)

Patient_dict = {'name':'vishesh', 'gender':'male', 'age':22, 'address':address1}

patient1 = Patient(**Patient_dict)

print(patient1)

print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)
