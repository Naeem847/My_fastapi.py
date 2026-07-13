# post methood is used to create a new resource on the server, while the put method is used to update an existing resource.
from fastapi import FastAPI, HTTPException
from pydanticc import BaseModel
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
#2 PUT Method - Update Item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):

    """
    This endpoint handles PUT requests to update an existing item.

    It uses a path parameter `item_id` to identify the item.

    It expects the updated item data in the request body.

    If the item exists, it updates it completely; otherwise, returns a 404 error.
    """

    # Check if item exists
    if item_id not in items_db:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    # Update item
    items_db[item_id] = item.dict()

    # Return updated item
    return {
        "message": "Item updated successfully",
        "item_id": item_id,
        "updated_item": item.model_dump()
    }

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.2", port=8000)