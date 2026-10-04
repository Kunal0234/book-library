from pydantic import BaseModel, Field
class BookSchema(BaseModel):
    title: str = Field(min_length=3)
    author: str
    category: str
    published_year: int = Field(gt=0)
    available: bool

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    category: str
    published_year: int
    available: bool

class DeleteResponse(BaseModel):
    message: str