# from fastapi import FastAPI,Path
from fastapi import FastAPI, Path, HTTPException, Query

from fastapi.responses import JSONResponse


from pydanticc import BaseModel ,Field ,computed_field

from typing import Annotated,List, Optional ,Literal
import json
# create a bject of fastapi

app=FastAPI()
print("patient management system API initialized")
class patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient in the DB', example='P001')]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City of the patient')]
    age: Annotated[int, Field(..., gt=0, lt=120,description='Age of the patient')]
    gender: Annotated[Literal['Male', 'Female','Other'],Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(...,gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(...,gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight / (self.height ** 2), 2)
        return bmi
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "underweight"
        elif 18.5 <= self.bmi < 25:
            return "normal"
        elif 25 <= self.bmi < 30:
            return "normal"
        else:
            return "obese"
def load_data():

    with open("patients.json") as f:
      
      data = json.load(f)

    return data
def save_data(data):

    with open("patients.json", "w") as f:
        json.dump(data, f)
@app.get("/")

def hello():
    return {"message":"patient management system API"}

@app.get("/about")

def about():
    return {"message":"A fully functional  API to manage your patient records built with FastAPI."}

@app.get("/view")
def view():
    data = load_data()
    return data

# make the end point to get patient by id
@app.get('/patient/{patient_id}')

def view_patient(patient_id: str=Path(...,description='ID of the patient in theh DB',
example='P001')):
    data = load_data()
    if patient_id in data:  
    # if patient_id['patient_id'] == patient_id:
      return data[patient_id]
    raise HTTPException(status_code=400, detail="Patient not found")
    

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height,weight or bmi')
,order: str=Query('asc', description='sort in asc or desc order')):

    
    valid_fields=['height','weight','bmi']
    
    if sort_by not in valid_fields:

        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:

        raise HTTPException(status_code=400, detail='Invalid order select between asc or desc')
    
    data = load_data()

    sort_order= True if order == 'desc' else False
    
    sorted_data =sorted(data.values(), key=lambda x: x.get(sort_by, 0),reverse=sort_order)
 
    return sorted_data

@app.post("/create")
def create_patient(patient: patient):

#   load the existing data from the JSON file
    data=load_data()
# check if the patient ID already exists in the data

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists")
    
# new patient data is added to the existing data
    data[patient.id] = patient.model_dump(exclude=['id'])

# save into the JSON file
    save_data(data)
    
    return JSONResponse(status_code=201,content={"patient created successfully"})