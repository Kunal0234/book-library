from sqlalchemy import  Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "sqlite:///./books.db"
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    category = Column(String)
    published_year = Column(Integer)
    available = Column(Boolean)

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# book = Book(
#     title="The Great Gatsby",
#     author="F. Scott Fitzgerald",
#     category="Fiction",
#     published_year=1925,
#     available=True
# )
# db.add(book)
# db.commit()
books = db.query(Book).all()

for book in books:
    print(book.id, book.title, book.author, book.category)

book = db.query(Book).filter(Book.id == 2).first()

print(book.title)
print(book.author)