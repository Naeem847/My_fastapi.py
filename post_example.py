from fastapi import FastAPI
# from flask import app
from pydantic import BaseModel
from typing import Optional
import uvicorn

class Item(BaseModel):
    name: str
    description: str
    price: float

    is_offer: Optional[bool] = None

app = FastAPI()

# int memory storage
items_db = {}

@app.post("/items/")

def create_item(item: Item):

    """this is a endpoint handle post request to
      create a new item in the items_db, it takes 
      an Item object as input and returns the created
        item with its id.  
    """
    # gemerate a new item id by incrementing the length of the items_db
    item_id = len(items_db) + 1
    # stoore the item in the items_db with the generated id
    items_db[item_id] = item
    
    return {"id": item_id, "item": item.model_dump()}

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="127.0.0.1", port=8000)