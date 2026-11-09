from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the book catalog API"}


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


books: dict[int, dict[str, int | str]] = {}
next_book_id = 1


@app.get("/books")
def list_books():
    # TODO: Return all books.
    return []


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Assign an ID, save the book, and return it.
    raise NotImplementedError


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the book or raise HTTPException with status 404.
    raise NotImplementedError
