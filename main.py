from typing import Union
import random, math
from fastapi import FastAPI,HTTPException,Path
from itertools import islice
from typing import Optional
app = FastAPI()



items=[{
    "id":1,
    "name":"Toster",
    "price":10,
    "description":"this is toster",
},
{
    "id":2,
    "name":"laptop",
    "price":100,
    "description":"laptop?",
},
{
    "id":3,
    "name":"pc",
    "price":200,
    "description":"pc is power",
},
{
        "id": 4,
        "name": "Smartphone",
        "price": 300,
        "description": "Latest model with great camera"
    },
    {
        "id": 5,
        "name": "Headphones",
        "price": 50,
        "description": "Noise-cancelling wireless headphones"
    },
    {
        "id": 6,
        "name": "Keyboard",
        "price": 25,
        "description": "Mechanical keyboard for gamers"
    },
    {
        "id": 7,
        "name": "Monitor",
        "price":150,
        "description": "24-inch Full HD display"
    },
    {
        "id": 8,
        "name": "Mouse",
        "price": 15,
        "description": "Ergonomic wireless mouse"
    },
    {
        "id": 9,
        "name": "Tablet",
        "price": 120,
        "description": "Portable and lightweight"
    },
    {
        "id": 10,
        "name": "Smartwatch",
        "price": 80,
        "description": "Tracks fitness and notifications"
    }
]

@app.get("/items/")
def search_item(name: str | None = None, min_price: int | None = None ,max_price: int | None = None,limit: int | None = None):
    def filter_items():
        for i in items:
            if name is not None and i["name"]!=name:
                continue
            if min_price is not None and i["price"]<= min_price:
                continue 
            if max_price is not None and i["price"]>=max_price:
                continue
            yield i
    filtered=filter_items()
    if limit is not None and limit>0:
        filtered=islice(filtered, limit)
    res=list(filtered)
    if not res:
        raise HTTPException(status_code=404, detail="Items not found")
    
    return res    
        
@app.get("/items/{item_id}")
def read_item_one(item_id: int = Path(..., gt=0)):
    for i in items:
        if i["id"]==item_id:
            return i    
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
def create_item(name: str,price: Optional[int] = None, description: Optional[str] = None):

    if len(name) < 3 or len(name) > 100:
        raise HTTPException(
            status_code=400,
            detail="Название должно быть больше двух символов или меньше ста символов"
        )
    if price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Цена должна быть больше нуля"
        )
    
    if description is not None and len(description) > 500:
        raise HTTPException(
            status_code=400,
            detail="Описание не должно быть больше 500 символов"
        )

    new_id = items[-1]["id"] + 1 if items else 1
    
    new_item = {
        "id": new_id,
        "name":name,
        "price":price,
        "description":description
    }
    items.append(new_item)
    
    return {"status": "success", "item": new_item}