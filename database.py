from sqlalchemy import  create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "sqlite:///./books.db"
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


Base.metadata.create_all(bind=engine)
