from book import Book
from manager import LibraryManager

def main():
    manager = LibraryManager("books_data.json")
    while True:
        print("\n1. Add Book\n2. Display Books\n3. Update Progress\n4. Delete Book\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            pages = int(input("Pages: "))
            book = Book(title, author, year, pages)
            manager.add_book(book)
        elif choice == "2":
            manager.display_books()
        elif choice == "3":
            title = input("Enter book title: ")
            progress = int(input("Enter progress (%): "))
            manager.update_progress(title, progress)
        elif choice == "4":
            title = input("Enter book title to delete: ")
            manager.delete_book(title)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()