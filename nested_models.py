from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address
address_dict={'city':'islamabad','state':'punjab','pin':'123434'}

address1=Address(**address_dict)

patient_dist={'name':'naeem','gender':'male','age':26,'address':address1}

patient1=Patient(**patient_dist)

print(patient1)

print(patient1.name)

print(patient1.address.city)

print(patient1.address.pin)