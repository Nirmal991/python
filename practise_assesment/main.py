products = [ 
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, 
    {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000, "quantity": 25} ,
    {"id": 4, "name": "Smartphone", "category": "Electronics", "price": 17800, "quantity": 12} ,
    {"id": 5, "name": "Smartphone", "category": "Electronics", "price": 31000, "quantity": 3} ,
    {"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50} ,
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 200000, "quantity": 2} ,
] 

id_counter = len(products)

# -----------------------------

def menu():
    menu_txt = '''1.Add Products
    2.View All Products
    3.Search Products
    4.Update Products
    5.Delete products
    6.Exit'''

    print("*********Product Managment System***************")
    print(menu_txt)
    try:
        choise = int(input("Enter the choise: "))
    except:
        choise = -1

    return choise
#-----------------------------------------

def add_prodct():
    ...
    try:
        print('Add Product')
        name = input("Name:  ").strip()
        if name == '':
            return 
        
        category = input("Category:  ").strip()
        if category == '':
            return

        price = float(input("Price:    " ))
        if price < 0:
            print("Price must me greater than 0")
            return

        quantity = int(input("Quantity:    "))
        if quantity < 0:
            print("Quantity must be >= 0")
            return
        products.append(dict(id=id_counter+1,name=name, category=category, price=price, quantity=quantity))
        id_counter+=1

    except ValueError:
        print("Please retry with numeric value")

# ===============================================================

def one_product(p):
    pid, name, category, price, quantity = p.values()
    print(f"ID:     :{pid}")
    print(f'Name        : {name}')
    print(f'Category    : {category}')
    print(f'Price       : {price}')
    print(f'Quantity    : {quantity}')
    print('-'*50) 

def many_products(product_list):
        print("-"*50)
        print(f"{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}")
        print("-"*50)
        for p in product_list:
            pid, name, category, price, qty = p.values()
            print(f"{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}")
        print("-"*60)

def view_products():
    if len(products) == 0:
        print("No products in the inventory. Please add first.")
    elif len(products) == 1:
        one_product(products[0])
    else:
        many_products(products)

def search_product():
    try:
        print("1. Search by id")
        print("1. Search by name")
        choise = int(input('Enter the id of the product to search: '))

        if choise == 1:
            pid = int(input("Enter th eid of product to search: "))
            search_product_by_id(pid)
        elif choise == 2:
            search_product_by_name()
        else:
            print('Invalid choise. Please try again. ')
    except:
        print('Please try again with integer input. ')

def search_product_by_id(pid):
     result = [p for p in products if p['id']==pid]
     if not result:
        print(f'No product found for id {pid}')
        return None

     one_product(result[0])
     return result[0]


def search_product_by_name(name):
    name = input("Enter the name of product")
    result = [p for p in products if p['name'] == name]
    if not result:
        print(f'No product found for name "{name}')
        return

    if len(result) == 1:
        one_product(result[0])
    else:
        many_products(result)

def edit_product():
    pass

def delete_product():
    try:
        pid = int(input("Enter the product id to delete: "))
        p = search_product_by_id(pid)
        if p is None:
            return

        ans = input("Are you sure you want to delete the product: [yes/no]")

        if ans == 'y':
            products.remove(p)
            print("Product deleted Successfully: ")

    except:
        print("Invalid type of input try again")

def main():
    while True:
        choise = menu()
        match choise:
            case 1:
                add_prodct()
            case 2:
                view_products()
            case 3:
                search_product()
            case 4:
                edit_product()
            case 5:
                delete_product
            case 6:
                break
            case _:
                print("Invalid choise. Retry")

if __name__ == '__main__':
    main()