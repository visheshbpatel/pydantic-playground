from pydantic import BaseModel

class Address(BaseModel):
    
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'              #default male
    age: int
    address: Address


address_dict = {"city": 'indore', "state":'madhya pradesh', "pin":'454545'}

address1 = Address(**address_dict)

Patient_dict = {'name':'vishesh', 'age':22, 'address':address1}

patient1 = Patient(**Patient_dict)

temp = patient1.model_dump()
temp_json = patient1.model_dump_json()

print(temp)
print(type(temp))
print()

print(temp_json)
print(type(temp_json))



temp = patient1.model_dump(include=['name', 'gender'])            #only include name and gender
temp = patient1.model_dump(exclude={'address':['state']})         #this excluded  state only
temp = patient1.model_dump(exclude_unset=True)                    #this exclude the unset default value for now male





