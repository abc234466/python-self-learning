from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    display_name: str
    description: str
    tax: Optional[float] = None


@app.post('/items')
async def create_item(item: Item):
    return item
