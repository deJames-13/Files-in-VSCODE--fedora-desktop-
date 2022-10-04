from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"data": "Home Directory in /"}

@app.get("/about")
def about():
    return {"data": "About Directory in /about"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="ID of the item.", gt=0, lt=2), name: str = None):
    for id in inventory:
        if inventory[id]["name"] == name:
            return inventory[id] 
    return inventory[item_id]

@app.get("/get_by_name")
def get_item(name: str):
    for id in inventory:
        if inventory[id]["name"] == name:
            return inventory[id] 
    return None

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular",
    }
    
}
