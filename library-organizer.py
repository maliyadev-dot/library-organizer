books = []
books.append("The Count of Monte Cristo")
books.append("Too Late")
books.append("The Housemaid")
print(books)
""" each book needs to be a dict with title, author, & years stored in list called library """
library = [
    {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "year": 1844},
    {"title": "Too Late", "author": "Colleen Hoover", "year": 2020},
    {"title": "The Housemaid", "author": "Freida McFadden", "year": 2021}
]

""" main menu: options like add, remove, list, search, sort, quit"""
def add_book():
    title = input("Whats the title?")
    author = input("Whats the author?")
    year = int(input("Whats the year?"))
    new_book = {"title": title, "author": author, "year": year}
    library.append(new_book)

def list_books():
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']})")

def remove_book():
    title_to_remove = input("Which book would you like to remove?")
    for book in library:
        if book['title'].lower() == title_to_remove.lower():
            library.remove(book)
            print("Book removed!")
            return
    print("Book not found.")

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Add book")
        print("2. List books")
        print("3. Remove book")
        print("4. quit")
        choice = input("Enter your choice (1-3)")
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            print("Deuces.")
            break
main_menu()
