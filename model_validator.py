from pydantic import BaseModel,EmailStr,model_validator

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
          if model.age>60 and 'emergency' not in model.contact_details:
                raise ValueError('Patient older then 60 must have an emergency contanct')
          return model

def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('updated')
patient_info={'name':'Ali', 'age':'61','email':'abc@hdfc.com','linkedin_url':'http://linkedin.com/1234','weight':87.1,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'92345678','emergency':'034434434'}}

patient1=Patient(**patient_info)

# print(patient1)

update_patient_data(patient1)

# print(patient1)

