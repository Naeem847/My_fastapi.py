from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
 
    @field_validator('email')

    @classmethod
    
    def email_validator(cls,value):
        
        valid_domains=['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def capetalize_name(cls,value):
        return value.upper()
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
         if 0< value <100:
              return value
         else:
              raise ValueError('age should be in between 0 and 100')

def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('updated')
patient_info={'name':'Ali', 'age':'25','email':'abc@hdfc.com','linkedin_url':'http://linkedin.com/1234','weight':87.1,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'92345678'}}

patient1=Patient(**patient_info)

# print(patient1)

update_patient_data(patient1)

# print(patient1)

