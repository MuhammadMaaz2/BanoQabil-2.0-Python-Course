# Library Management System
# Author: [Your Name]
# Roll Number: [Your Roll Number]
# Email: [Your Email Address]

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def search_book(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print("Book found:")
                print(book)
                found = True
                break
        if not found:
            print("Book not found.")

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            book = Book(title, author, genre)
            library.add_book(book)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter title to search: ")
            library.search_book(title)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
