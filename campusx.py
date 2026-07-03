import json

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