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

temp = patient1.model_dump(include=['name','gender'])

temp = patient1.model_dump(exclude=['name'])

temp = patient1.model_dump(exclude={'address':['city']})

print(temp)

print(type(temp))