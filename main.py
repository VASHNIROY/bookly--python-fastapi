from fastapi import FastAPI,Header,status
from fastapi.exceptions import HTTPException
from typing import Optional
from typing import List
from src.books.schemas import BookCreateModel,Book,BookUpdateModel
from src.books.book_data import books
app = FastAPI()
