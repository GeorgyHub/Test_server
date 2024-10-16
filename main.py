from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

# Основа приложения
app = FastAPI()

# Модель
class Message(BaseModel):
    description: str
    

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Домашняя функция
@app.get("/home")
def read_root():
    return {"data": "Hello World"}

# Функция переписки
@app.post("/message")
async def message():
    return {"Ok": True}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}