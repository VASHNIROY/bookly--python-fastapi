from fastapi import APIRouter,status,Header
from fastapi.exceptions import HTTPException
from typing import Optional
from typing import List
from book_data import books
from schemas import Book,BookCreateModel,BookUpdateModel
book_router = APIRouter()

@book_router.get("/")
async def hello_word():
    return {"message": "Hello World"}
    
@book_router.get("/greet")
async def check_name(name: Optional[str] = "Vashni",age: int = 10):
    return {"name": f"your name is {name}","age": age}

@book_router.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {"title": book_data.title,"author": book_data.author}

@book_router.get('/',response_model=List[Book])
async def get_all_books():
    return books

@book_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Book not found")

@book_router.patch('/book/{book_id}')
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['genre'] = book_update_data.genre
            book['currency'] = book_update_data.currency
            book['stock'] = book_update_data.stock
            book['rating'] = book_update_data.rating
            book['author'] = book_update_data.author
            book['price'] = book_update_data.price
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')

@book_router.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

@book_router.get('/get_headers')
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers