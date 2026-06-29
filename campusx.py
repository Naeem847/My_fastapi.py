from fastapi import FastAPI

# create a bject of fastapi
app=FastAPI()

@app.get("/")

def hello():
    return {"message":"Hello, World!"}

@app.get("/about")

def about():
    return {"message":"campusx is an education plateform where you can learn Ai"}

