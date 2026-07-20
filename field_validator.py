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
    
patient_info={'name':'Ali', 'age':'25','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1234','weight':87.1,'contact_details':{'phone':'92345678'}}

patient1=Patient(**patient_info)
