import subprocess

def menu():
    print("*** MAIN MENU ***")
    print("=================")
    print("0. Exit")
    print("1. Add a book record")
    print("2. View all books")
    print("3. Edit a book record")
    print("4. Delete a book")

    try:
        choise = int(input("Enter Your Choise: "))
        if choise > 4 or choise < 0:
            choise = -1
    except: 
        choise = -1

    return choise

books = [
    {"id" :819, "title" :"Let us C", "author": "Y Kanitkar", "price": 499.0},
    {'id': 33, 'title': 'Python Unleashed', 'author': 'John MIller', 'price': 999.0},
    {'id': 298, 'title': 'Java made easy', 'author': 'Rajesh Rao', 'price': 1499.0},
]


def add_book():
    b = {}
    print("Enter the book details: ")

    while True:
        try:
            b["id"] == int(input("ID: "))
        except: 
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu.")

        if user_input != 'r':
            return
        else:
            break

    b['title'] = input("Title: ")
    b['author'] = input("Author: ")

    try:
        b['price'] = float(input('Price: '))
    except:
        print('Invalid value for price. Value was set to 0.0')
        b['price'] = 0

    books.append(b)

def view():
    print("-"*98)
    print(f"{"ID":^10} {"Title":<35} {"Author":<35} {"Price":>15}")
    print("-"*98)
    for b in books:
        print(f"{b['id']:^10} {b['title']:<35} {b['author']:<35} {b['price']:>15.2f}")
    print("-"*98)