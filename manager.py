import json
from typing import List
from book import Book
from typing import Optional


class LibraryManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, title: str, author: str, year: int, pages: int, zip_code: Optional[str] = None) -> None:
        book = Book(title, author, year, pages, zip_code=zip_code)
        self.books.append(book)
        self.save_books()

    def display_books(self) -> None:
        for i, book in enumerate(self.books, start=1):
            zip_code = book.zip_code if book.zip_code else "N/A"
            print(f"{i}. {book.title} by {book.author} ({book.year}) - Pages: {book.pages}, Progress: {book.progress}%, Zip Code: {zip_code}")

    def update_progress(self, title: str, progress: int, zip_code: Optional[str] = None) -> None:
        for book in self.books:
            if book.title.lower() == title.lower():
                book.progress = progress
                if zip_code:
                    book.zip_code = zip_code  # Update zip code if provided
                self.save_books()
                print("Progress updated successfully.")
                return
        print("Book not found.")

    def delete_book(self, title: str) -> None:
        original_count = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        if len(self.books) < original_count:
            self.save_books()
            print("Book deleted successfully.")
        else:
            print("Book not found.")
