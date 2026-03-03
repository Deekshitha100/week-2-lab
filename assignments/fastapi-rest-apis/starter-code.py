from fastapi import FastAPI
from pydantic import BaseModel

# Task 1: create FastAPI app and basic route
app = FastAPI()

@app.get("/")
def read_root():
    # return a simple greeting message
    return {"message": "Hello, FastAPI!"}

# Task 2: path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # return the item_id and optional query parameter
    return {"item_id": item_id, "q": q}

# Task 3: Pydantic model and POST endpoint
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.post("/items/")
def create_item(item: Item):
    # simply echo back the item data
    return item

# Additional tasks can be added below as needed
