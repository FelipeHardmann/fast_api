# main.py 
from fastapi import FastAPI 
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from os import path
from fastapi.responses import FileResponse

# @app.get("/users/{type}/{id}") 
# async def get_user(type: str, id: int): 
#     return {'type': type, 'id': id} 

# @app.post('/users')
# async def create_user(name: str = Body(...), age: int = Body(...)):
#     return {'name': name, 'age': age}



# class User(BaseModel):
#     name: str
#     age: int
    


# app = FastAPI()

# @app.post('/users')
# async def create_user(user: User):
#     return user 



# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
    

# app = FastAPI()

# @app.post('/items')
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.price:
#         price_with_tax = item.price + item.tax
#         item_dict.update({'price_with_tax': price_with_tax})
#     return item_dict



app = FastAPI()

@app.get('/gato')
async def get_gato():
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = path.join(root_directory, 'gato.jpg')
    return FileResponse(picture_path)