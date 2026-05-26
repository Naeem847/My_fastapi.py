from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
# create a fastapi instance
app= FastAPI(
    title="My FastAPI Application",
    description="this is a simple FastAPI application",
    version="1.0.0"
)
# define a pydantic model from a request body
class textRequest(BaseModel):
    text: str
    uppercase: Optional[bool] = False
# define a pydantic model for the responce
class textResponse(BaseModel):
    original_text: str
    text_length: int
# this handle get request to the root endpoint("/")
@app.get("/")   # this handle get request to the root endpoint("/")
def read_root():
    return {"message": "Welcome to our text processing API!"}
# define a post end point for the processing text
@app.post("/process-text/",response_model=textResponse)  # this handle get request to the "/hello/{name}" endpoint
def process_text(request: textRequest):
    # get the text from the request and process it based on the uppercase flag  
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")  
    processed_text = text.upper() if request.uppercase else text
# crrate the responce
    response = textResponse(
        original_text=processed_text, 
        text_length=len(processed_text)
    )
    return response
    # return textResponse(original_text=text, text_length=len(text))
if __name__ == "__main__":
    # start the server using uvicorn
    uvicorn.run("my_firstproject:app", host="127.0.0.1", port=8000, reload=True)

