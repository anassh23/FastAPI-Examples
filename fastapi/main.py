from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    name: str
    description: str
    author: str
    id: int


books = {
    0: Book(name="Rich dad poor dad", description="very good", author="Robert", id=0),
    1: Book(name="7 habits for wealthy people", description="introducing the 7 habits for people", author="ME", id=1),
    2: Book(name="Elon Musk", description="Excellent", author="Anas", id=2),
}


@app.get("/book/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]


# ME

# @app.post("/book")
# # def add_book(name: str, description: str, author: str):
# def add_book(book: Book):
#     if book.name in books:
#         HTTPException(status_code=400, detail=f"book with the name{book.name=} already exists")
#
#     books[book.id] = book
#     return {"added": book}

# ClaudeAI
@app.post("/book")
def add_book(book: Book):
    if any(b.name == book.name for b in books.values()):
        raise HTTPException(status_code=400, detail=f"Book with the name '{book.name}' already exists")

    new_id = max(books.keys(), default=-1) + 1
    book.id = new_id
    books[new_id] = book
    return {"added": book}


@app.put("/book/{book_id}")
def Update_book(book_id: int, book: Book):
    if book.name not in books:
        HTTPException(status_code=404, detail=f"book with the name{book.name=} does not exist")

    books[book_id] = book
    return {"message": "Book updated successfully"}


@app.delete("/book/{book_id}")
def delete_book(book_id: int, book: Book):
    if book.name not in books:
        HTTPException(status_code=404, detail=f"book with the name{book.name=} does not exist")

    deleted_book = books.pop(book_id)
    return {"message": "Book deleted successfully"}


@app.get("/books")
def get_all_books():
    return books


