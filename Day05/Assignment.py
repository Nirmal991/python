# import re
# def manage_bookstore_inventory(inventory, action, book_title, quantity=0):
#     existing_quantity = inventory.get(book_title)
#     if action == 'add':
#         inventory.update({book_title: existing_quantity+quantity})
#         return inventory
#     elif action == 'sell':
#         if existing_quantity == 0:
#             print(f"Error: Book '{book_title}' not found in inventory.")
#         elif existing_quantity == None or existing_quantity < quantity:
#             print(f"Error: Insufficient stock for '{book_title}'")
#         else:
#             existing_quantity -= quantity
#             if existing_quantity == 0:
#                 inventory.pop(book_title)
#             print(f"Sold! {book_title =} and {quantity =}")
#         return inventory
#     elif action == "lookup":
#         print(f"{book_title =} and {existing_quantity=}")

# class InvalidPhoneNumberError(Exception):
#     pass

# def register_contact(phonebook, name, phone_input):
#     name_pattern = r"/(^[a-zA-Z][a-zA-Z\s]{0,20}[a-zA-Z]$)/"
#     phone_pattern = r"/d{6,11}"

#     a = re.search(phone_pattern, phone_input)
#     b = re.search(name_pattern, name)

#     if a == None:
#         raise InvalidPhoneNumberError("Invalid Phone Number")

#     if b == None:
#         raise Exception("Invalid name")
#     phonebook.update({name: phone_input})
#     return phonebook


def compile_feedback(ratings_dict):
    result = {}
    for sub, rating in ratings_dict.items():
        valid = []
        try:
            for rate in rating:
                value = float(rate)
            valid.append(value)
            print(f'**{value}')
        except (TypeError, ValueError):
            print(f"Invalid rating value '{rate}' in course '{sub}' skipped")

    try:
        avg = sum(valid) / len(valid)
        result[sub] = round(avg, 2)
        print(f'**{result}')
    except ZeroDivisionError:
        print(f"No valid ratings found for course '{sub}'. Rating set to 0.0")
        result[sub] = 0.0
    return result

def main():
    # inventory = {"Python Basics": 10, "Learning AI": 5}
    # print(inventory)
    # manage = manage_bookstore_inventory(inventory,"add","Python Basics", 5)
    # print(manage)
    # manage = manage_bookstore_inventory(inventory, "loockup", "Python Basics", 20)
    # print(manage)

    feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

    res = compile_feedback(feedback_data)
    print(res)

main()