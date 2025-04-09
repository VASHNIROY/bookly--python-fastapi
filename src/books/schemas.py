from pydantic import BaseModel


class BookCreateModel(BaseModel):
    title: str
    author: str
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    price:float
    currency: str
    stock: int
    rating: float
    isbn: str
    published_year: float

class BookUpdateModel(BaseModel):
    title: str
    author: str
    genre: str
    price:float
    currency: str
    stock: int
    rating: float
