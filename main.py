from typing import Union
import random, math
from fastapi import FastAPI,Query
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/about")
def about():
    return {"name":"Kirill",
            "surname":"Godov",
            "group": "Т-323901-НТ"}

@app.get("/rnd")
def rnd():
    return {random.randint(0, 10)}

@app.post("/t_square")
def t_square(a: int=Query(gt=0), b:int=Query(gt=0), c:int=Query(gt=0)):
    if a+b<=c or a+c<=b or b+c<=a:
        return{"error": "not triangle"}
    else:
        p=(a+b+c)/2
        return {math.sqrt(p*(p-a)*(p-b)*(p-c))} 
