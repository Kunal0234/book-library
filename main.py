from fastapi import FastAPI, HTTPException
from database import SessionLocal
from models import Book
from schemas import BookSchema
app = FastAPI()



@app.get("/")
def func():
    return {'message':"Hello world"}

 

@app.post("/book")
def insert_book_data(book_data: BookSchema):
    db = SessionLocal()

    book = Book(
        title=book_data.title,
        author=book_data.author,
        category=book_data.category,
        published_year=book_data.published_year,
        available=book_data.available
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    result = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "category": book.category,
        "published_year": book.published_year,
        "available": book.available
    }

    db.close()

    return result

@app.get("/books")
def show_books():
  db = SessionLocal()
  books = db.query(Book).all() 
  

  db.close()
  return books 



@app.get("/books/{book_id}")
def show_one_book(book_id: int):
    db = SessionLocal()

    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    result = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "category": book.category,
        "published_year": book.published_year,
        "available": book.available
    }

    db.close()

    return result

@app.put("/books/{book_id}")
def update_book(book_id: int, update_data: BookSchema):
    db = SessionLocal()

    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.title = update_data.title
    book.author = update_data.author
    book.category = update_data.category
    book.published_year = update_data.published_year
    book.available = update_data.available

    db.commit()
    db.refresh(book)

    result = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "category": book.category,
        "published_year": book.published_year,
        "available": book.available
    }

    db.close()

    return result
    
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()

    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    db.close()

    return {"message": "Book successfully deleted"}

