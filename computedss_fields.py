from pydantic import BaseModel,EmailStr,computed_field

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    height:float #mters
    weight:float #kg
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self):

        bmi= round(self.weight/(self.height**2),2)

        return bmi
    
def update_patient_data(patient: Patient):
        
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('BMI',Patient.bmi)
        print('updated')
patient_info={'name':'Ali', 'age':'61','height':'1.72','email':'abc@hdfc.com','linkedin_url':'http://linkedin.com/1234','weight':87.1,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'92345678','emergency':'034434434'}}

patient1=Patient(**patient_info)

# print(patient1)

update_patient_data(patient1)

# print(patient1)

