from pydantic import BaseModel,Field
from fastapi import FastAPI,HTTPException

app = FastAPI()

temp_db = []

@app.get("/")
def func():
    return {'message':"Hello world"}

class Book(BaseModel):

    title:str
    author:str
    category:str
    published_year:int
    available:bool 

@app.post("/book")
def insert_book_data(book_data : Book):
  temp_db.append(book_data)
  return book_data

@app.get("/books")
def show_books():
   return temp_db

@app.get("/books/{book_id}")
def show_one_book(book_id: int):
    if book_id < 0 or book_id >= len(temp_db):
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return temp_db[book_id]

@app.put("/books/{book_id}")
def update_book(book_id: int, update_data: Book):
    if book_id < 0 or book_id >= len(temp_db):
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    temp_db[book_id] = update_data

    return update_data
    
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(temp_db):
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    temp_db.pop(book_id)

    return {"message": "Book successfully deleted"}

