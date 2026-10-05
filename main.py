from fastapi import FastAPI, HTTPException
from database import SessionLocal
from models import Book
from schemas import BookSchema, BookResponse, DeleteResponse
from typing import Optional

app = FastAPI()



@app.post("/book",response_model=BookResponse)
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
    db.close()

    return book
@app.get("/books", response_model=list[BookResponse])
def show_books(
    category: Optional[str] = None,
    author: Optional[str] = None,
    available: Optional[bool] = None,
    skip: int = 0,
    limit: int = 10,
    sort_by: Optional[str] = None
):
    db = SessionLocal()
    query = db.query(Book)

    if category:
        query = query.filter(Book.category == category)

    if author:
        query = query.filter(Book.author == author)

    if available is not None:
        query = query.filter(Book.available == available)
  

    if sort_by == "title":
        query = query.order_by(Book.title)

    elif sort_by == "year":
        query = query.order_by(Book.published_year)

    books = query.offset(skip).limit(limit).all()   

    db.close()
    return books

@app.get("/test")
def test(category: str):
    return {"category": category}

@app.get("/books/{book_id}",response_model=BookResponse)
def show_one_book(book_id: int):
    db = SessionLocal()

    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )


    db.close()

    return book

@app.put("/books/{book_id}",response_model=BookResponse)
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

    

    db.close()

    return book
    
@app.delete("/books/{book_id}", response_model=DeleteResponse)
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

