from pydantic import BaseModel,Field
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def func():
    return {'message':"Hello world"}

class Book(BaseModel):

    title:str
    author:str
    category:str
    published_year:int
    available:bool 

