from typing import Optional, Dict

class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, progress: int = 0):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.progress = progress

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "pages": self.pages,
            "progress": self.progress,
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        return Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            pages=data["pages"],
            progress=data.get("progress", 0),
        )