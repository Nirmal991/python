import subprocess

def menu():
    """
    Display a set of options to the user,
    accept the user's choice,
    do a basic validation
    if correct value, return the same
    else return -1
    """
    print("=================")
    print("0. Exit")
    print("1. Add a book record")
    print("2. View all books")
    print("3. Edit a book record")
    print("4. Delete a book")

    try:
        choice = int(input("Enter the choice: "))
        if choice < 0 or choice > 4:
            choice = -1
    except:
        choice = -1
    return choice

books = [
    {"id" :819, "title" :"Let us C", "author": "Y Kanitkar", "price": 499.0},
    {'id': 33, 'title': 'Python Unleashed', 'author': 'John MIller', 'price': 999.0},
    {'id': 298, 'title': 'Java made easy', 'author': 'Rajesh Rao', 'price': 1499.0},
]

def add_product():
    b = {}
    print("Enter the details to add: ")
    while True:
        try:
            b["id"] = int(input("ID: "))
        except:
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu.")

            if user_input != 'r':
                return
            else:
                break

        b["title"] = input("Tittle:   ")
        b["author"] = input("Author:   ")

        try:
            b["price"] = float(input("Price:      "))
        except:
            print('Invalid value for price. Value was set to 0.0')
            b['price'] = 0

        books.append(b)

def view_books():
    print("-"*90)
    print(f"{"ID":^10} {"Title":<35} {"Author":<35} {"Price":>15}")
    print("-"*90)
    for b in books:
        print(f"{b["id"]:^10} {b["title"]:<35} {b["author"]:<35} {b["price"]:>15}")
    print("-"*90)

def edit_products():
    while True:
        try:
            book_id = int(input("Enter book id to edit: "))
        except: 
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu: ")

            if user_input != 'r':
                return
            else:
                break

        book_ids = [b["id"] for b in books]
        print(book_ids)
        if book_id not in book_ids:
            print("No such book found")
            return

        the_book = [b for b in books if b["id"] == book_id][0]
        _, title, author, price = the_book.values()

        _title = input(f'Title:  ({title}) ')
        if _title == "":
            _title = title

        _author = input(f"Author:  ({author})")
        if _author == "":
            _author = author

        _price = input(f"Price:  ({price})")
        if _price == "":
            _price = price
        else:
            try:
                _price = float(_price)
            except:
                print("Invalid value for price. Remains unchanged.")
                _price = price

        the_book["title"] = _title
        the_book["author"] = _author
        the_book["price"] = _price

        print("The book is updated successfully")

def delete():
    while True:
        try:
            book_id = int(input("Enter the book Id to delete: "))
        except:
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu: ")

            if user_input != 'r':
                return
        else:
            break

        book_ids = [b["id"] for b in books]
        if book_id not in book_ids:
            print("No such book found")
            return

        the_book = [b for b in books if b["id"] == book_id][0]
        print("Book found!")
        print(f"ID          : {the_book["id"]}")
        print(f"Title       : {the_book["title"]}")
        print(f"Author      : {the_book["author"]}")
        print(f"Price       : {the_book["price"]}")

        print()
        ans = input("Are you sure you want to delete [yes/no]")

        if ans.strip().lower() == 'yes':
            books.remove(the_book)
            print("Book deleted successfully")
        else:
            print("Book are not deleted")


def main():
    while True:
        subprocess.call(["cls"], shell=True)
        choice = menu()
        match choice:
            case -1:
                print("Invalid choice please enter a valid number")
            case 0:
                break
            case 1:
                add_product()
            case 2:
                view_books()
            case 3:
                edit_products()
            case 4: 
                delete()

        print()
        input("Hit RETURN/Enter key to continue")
    print("BYE!")

print("-"*80)
main()

