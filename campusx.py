import json

# from fastapi import FastAPI,Path
from fastapi import FastAPI

# create a bject of fastapi

app=FastAPI()

def load_data():

    with open("patients.json") as f:
      
      data = json.load(f)

    return data

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

def view_patient(patient_id: str):

    data = load_data()

    # if patient_id in data:  
    if patient_id['patient_id'] == patient_id:

        return data[patient_id]
    
    return {"error":"patient not found"}

