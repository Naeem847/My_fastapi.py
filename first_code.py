from fastapi import FastAPI
 
import uvicorn

app= FastAPI(
    title="My FastAPI Application",
    description="this is a simple FastAPI application",
    version="1.0.0"

)
@app.get("/")   # this handle get request to the root endpoint("/")
def read_root():
    
    return {"message": "Welcome to my FastAPI application!"}
@app.get("/hello/{name}")  # this handle get request to the "/hello/{name}" endpoint

def read_item(name: str):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    # start the server using uvicorn
    uvicorn.run("my_firstproject:app", host="127.0.0.1", port=8000, reload=True)

