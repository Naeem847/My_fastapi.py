# def insert_patient_data(name:str, age:int):

#      if type(name) == str and type(age) == int:
#        if age<0:
#             raise ValueError("Age cannot be negative")
#        else:

#         print(name)
#         print(age)

#         print("insert into database")
#      else:
#         raise TypeError("Incorrect data type")  
      
# insert_patient_data('ali', 25)


# # # update patient data

# def update_patient_data(name:str, age:int):

#     if type(name) == str and type(age) == int:
#          if age<0:
#           raise ValueError("Age cannot be negative")
#          else:
#           print(name)
#           print(age)

#           print("update in database")
#     else:
#             raise TypeError("Incorrect data type")  
      
# update_patient_data('ali', 25)
   
from pydantic import BaseModel,AnyUrl,Field

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:Annotated[str,Field(max_length=50,tile='Name of the patient',description='give the same of the patient' \
    'in lessthen 5 charts',examples=['ali','aliya'])]

    age: int =Field(gt=0 , lt=120)
    linkedin_url:AnyUrl
    # email:EmailStr
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None, description='is the patient married or not')]
    alergies:Annotated[Optional[List[str]],Field(default=None, max_length=5)]
    contact_details:Dict[str,str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.alergies)
    print(patient.married)
    # print(patient.email)
    print("inserted")
    print("insert into database")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.alergies)
    print(patient.married)
    print(patient.weight)
    print(patient.linkedin_url)
    # print(patient.email)
    print("updated")
    print("update in database")

patient_info={'name':'Ali', 'age':'25','linkedin_url':'http://linkedin.com/1234','weight':87.1,'contact_details':{'emal':'asdf@gmail.com','phone':'92345678'}}

patient1=Patient(**patient_info)


update_patient_data(patient1)

# ,'alergies':['pollen','Dust'] ,


