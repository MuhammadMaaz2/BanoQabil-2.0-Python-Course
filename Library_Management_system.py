# Library Management System
# Author: Muhammad Maaz
# Roll Number: 
# Email: hafeezmaaz43@gmail.com

# Problem Statement:
# Create a simple library management system that allows users to add, remove, and search for books in the library.

# Function to add a book to the library
def add_book(library, book):
    library.append(book)
    print(f"Book '{book}' added to the library.")

# Function to remove a book from the library
def remove_book(library, book):
    if book in library:
        library.remove(book)
        print(f"Book '{book}' removed from the library.")
    else:
        print(f"Book '{book}' not found in the library.")

# Function to search for a book in the library
def search_book(library, book):
    if book in library:
        print(f"Book '{book}' found in the library.")
    else:
        print(f"Book '{book}' not found in the library.")

# Main function
def main():
    library = []  # Initialize an empty list to store books

    # Menu for the library management system
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book = input("Enter the name of the book to add: ")
            add_book(library, book)
        elif choice == "2":
            book = input("Enter the name of the book to remove: ")
            remove_book(library, book)
        elif choice == "3":
            book = input("Enter the name of the book to search: ")
            search_book(library, book)
        elif choice == "4":
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
