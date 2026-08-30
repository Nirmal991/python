def menu():
    print("*** MAIN MENU ***")
    print("=================")
    print("0. Exit")
    print("1. Add a book record")
    print("2. View all books")
    print("3. Edit a book record")
    print("4. Delete a book")

    choice = int(input("Enter your choice: "))

    if choice < 0 or choice > 4:
        choice = -1

    return choice


def main():
    while True:
        user_choice = menu()

        if user_choice == 0:
            break

        if user_choice == 1:
            print("Adding book feature is not ready")

        elif user_choice == 2:
            print("Viewing book choice is not ready")

        elif user_choice == 3:
            print("Editing book feature is not ready")

        elif user_choice == 4:
            print("Deleting book choice is not ready")

        else:
            print("Invalid choice! Please retry with valid value.")

    print("BYE!")


print("=" * 80)
main()