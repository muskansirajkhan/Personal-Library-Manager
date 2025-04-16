from typing import Optional, Dict

class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, progress: int = 0, zip_code: Optional[str] = None):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.progress = progress
        self.zip_code = zip_code  # Added zip_code

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "pages": self.pages,
            "progress": self.progress,
            "zip_code": self.zip_code,  # Added zip_code to dictionary
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        return Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            pages=data["pages"],
            progress=data.get("progress", 0),
            zip_code=data.get("zip_code", None),  # Added zip_code to from_dict
        )
