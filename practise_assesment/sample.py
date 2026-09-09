import json 
import csv

products = [
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}
]

id_counter = 3

def print_menu():
    menu_txt = '''
    0.exit
    1.ADD Product
    2.View Product
    3.Search Product
    4.Edit Product
    5.Delete Product
    6. Load to txt
    7. txt to cmd
    8. load to json
    9. json to smd 
    10. load to csv 
    11. csv to cmd
    '''
    print("***********PRODUCT MANAGMENT SYSTEM************")
    print(menu_txt)
    try:
        choice = int(input("Enter the choice of user:  "))
        
        if choice < 0 or choice > 11:
             choice = -1
        return choice
    except Exception:
        choice = -1
        
     
def add_product():
    global id_counter
    print("Enter the Product Details:  ")
    while True:
        id_counter += 1
        curr_Id = id_counter
        
        try:
            name = str(input("Enter the name of Product:  "))
            while name == "":
                print("Name cannot be left empty")
                name = input("Name:     ")
        except Exception:
            print("Name must be a String")
            
        try:
            category  = str(input("Enter the category  of Product:  "))
            while category  == "":
                print("category cannot be left empty")
                category  = input("category:     ")
        except Exception:
            print("category must be a String")
            
        while True:
            try:
                price = float(input("Enter the price:   "))
                if price <= 0:
                    print("Price must be greater than 0 ")
                    continue
                break
            except Exception:
                print("Price must be an Number")
                
        while True:
            try:
                qunatity = float(input("Enter the qunatity:   "))
                if qunatity <= 0:
                    print("qunatity must be greater than 0 ")
                    continue
                break
            except Exception:
                print("Quantity must be an Number")
                
        data = dict(id=curr_Id, name=name, category=category, price=price, qunatity=qunatity)
        products.append(data)
        
        print(f"Product with id: {curr_Id} Added successfully")
        
        ans = input("Add more Product:  [y/n]")
        
        if ans.strip().lower() == 'n':
            break
        
    
def print_one_product(products):
        products = products[0]
        pid,name,category,price,quantity = products.values()
        
        print(f"ID:          {pid}")
        print(f"Name:          {name}")
        print(f"Category:          {category}")
        print(f"Price:          {price}")
        print(f"Quantity:          {quantity}")

def print_many_product(products):
    print("-"*80)
    print(f"{'ID':^5} {'Name':<20} {'Category':<20} {'Price':<15} {'Quantity':<15}")
    print("-"*80)
    for p in products:
        pid, name, category, price, quantity = p.values()
        print(f"{pid:^5} {name:<20} {category:<20} {price:<15} {quantity:<20}")
    print("-"*80)
    
def view_product(products):
    if len(products) == 0:
        print("Add the Products First") 
    elif len(products) == 1:
        print_one_product(products) 
    else:
        print_many_product(products)
        
def search_products():
    result = []
    search_term = input("Enter the term from which we want to search:  ")
    if search_term.isdigit():
        search_item = int(search_term) # int not float
        
        product = [p for p in products if p['id'] == search_item]
        if not products:
            print("Product with this Id is not found")
            return []
            
        return product
    else:
        search_item = search_term.strip().lower()
        
        for p in products:
            if search_item in p['name'].strip().lower():
                result.append(p)
        return result
        
# def edit_Product():
    edit_id = input("Enter the Id you want to edit:   ")

    # Convert ID to integer
    if not edit_id.isdigit():
        print("Id must be a number")
        return

    edit_id = int(edit_id)

    product = [p for p in products if p['id'] == edit_id]

    if not product:
        print("Product with this id not found")
        return

    product = product[0]

    edit_menu = '''
    1. Edit name
    2. Edit Category
    3. Edit price
    4. Edit Quantity
    '''

    print(edit_menu)

    while True:
        choice = input("Enter your choice to update: ")

        if choice == '1':
            _name = input("Name:    ")

            while _name.strip() == "":
                print("Name cannot be empty")
                _name = input("Name:    ")

            product['name'] = _name
            print("Name updated successfully")
            break

        elif choice == '2':
            _category = input("Enter the category of Product:  ")

            while _category.strip() == "":
                print("Category cannot be left empty")
                _category = input("Category:     ")

            product['category'] = _category
            print("Category updated successfully")
            break

        elif choice == '3':
            while True:
                try:
                    _price = float(input("Enter the price:   "))

                    if _price <= 0:
                        print("Price must be greater than 0")
                        continue

                    product['price'] = _price
                    print("Price updated successfully")
                    break

                except ValueError:
                    print("Price must be a number")

            break

        elif choice == '4':
            while True:
                try:
                    _quantity = int(input("Enter the quantity:   "))

                    if _quantity <= 0:
                        print("Quantity must be greater than 0")
                        continue

                    product['quantity'] = _quantity
                    print("Quantity updated successfully")
                    break

                except ValueError:
                    print("Quantity must be a number")

            break

        else:
            print("Enter a valid choice")    
            
def edit_Product():
    edit_id = input("Enter the Id you want to edit:  ")
    
    if not edit_id.isdigit():
        print("Id must be an number")
        return
    
    edit_id = int(edit_id)
    
    product = [p for p in products if p['id'] == edit_id]
    
    if not product:
        print("Product with this Id is not Available")
        return
    
    product = product[0]
    
    edit_menu = '''
    1. Update Name
    2. Update Category
    3. Update price
    4. Update quantity
    '''
    
    print(edit_menu)
    
    while True:
        choice = input("Enter the choice you want to edit:  ")
        
        if choice == '1':
            try:
                _name = input("Name:    ")
                while _name == "":
                    print("Name Cannot be empty")
                    _name = input("Name:    ")
                product['name'] = _name
                print("Name changed Successfully...")
                break
            except Exception:
                print("Enter the valid value for name")
                
                
        elif choice == '2':
            try:
                _category = input("Category:    ")
                while _category == "":
                    print("Category Cannot be empty")
                    _category = input("Category:    ")
                product['category'] = _category
                print("Category changed Successfully...")
                break
            except Exception:
                print("Enter the valid value for Category")
                
        elif choice == '3':
            while True:
                try: 
                    _price = float(input("Price:     "))
                    if _price <= 0:
                        print("Price cannot be less than 0")
                        continue
                    product['price'] = _price
                    print("Product Updated Successfully")
                    break
                except Exception:
                    print("Price must be a Number")
            break
            
        elif choice == '4':
            while True:
                try: 
                    _quantity = int(input("Quantity:     "))
                    if _quantity <= 0:
                        print("Quantity cannot be less than 0")
                        continue
                    product['quantity'] = _quantity
                    print("Quantity Updated Successfully")
                    break
                except Exception:
                    print("Quantity must be a Number")
            break
        else: 
            print("Enter a Valid choice")
            
            
def delete_product():
    
    del_id = input("Enter the Id you want to edit:   ")
    
        # Convert ID to integer
    if not del_id.isdigit():
        print("Id must be a number")
        return
    
    del_id = int(del_id)
    
    product = [p for p in products if p['id'] == del_id]
    
    if not product:
        print("Product with this id not found")
        return
    
    product = product[0]
    
    ans = input("Are you sure you want to delete the product:  [y/n]")
    if ans.strip().lower() == 'y':
        products.remove(product)
    else:
        print("NOT DELETED")

def load_to_txt():
    filename = input("Enter the name of file in txt format:  ")
    try:
        with open(filename, 'wt', encoding='utf-8') as file:
            for p in products:
                file.write(
                    f"{p['id']}|"
                    f"{p['name']}|"
                    f"{p['category']}|"
                    f"{p['price']}|"
                    f"{p['quantity']}\n"
                )
    except FileNotFoundError:
        print("File Not Available")
            
def txt_cmd(): # see again
    product = []
    filename = input("Enter the name of file:  ")
    headers = ('id', 'name', 'category', 'price', 'quantity')
    with open(filename, 'r') as file:
        for product in file:
            part = product.strip().split('|')
            p = dict(zip(headers, part))
            products.append(p)
    print(products)
    
# def load_to_json():
#     filename = input("Enter the nameof file:   ")
#     with open(filename, 'wt', encoding='utf-8') as file:
#         json.dump(products, file, indent=4)
        
def load_to_json():
    filename = input("Enter the nameof file:   ")
    with open(filename, 'wt', encoding='utf-8') as file:
        data = json.dumps(products, indent=4)
        file.write(data)
        
def json_to_cmd():
    filename = input("Enter th ename of file:   ")
    with open(filename, 'r', encoding='utf-8') as file:
        res = json.load(file)
        print(res)
        
# def json_to_cmd():  # loads except string not file
#     filename = input("Enter th ename of file:   ")
#     with open(filename, 'r', encoding='utf-8') as file:
#         res = json.loads(file)
#         print(res)

def load_csv():
    filename = input("Enter the name of file:   ")
    
    with open(filename, 'wt', encoding='utf-8') as file:
        writer = csv.DictWriter(file, ['id', 'name', 'category', 'price', 'quantity'], delimiter='|', lineterminator='\n')
        writer.writeheader()
        writer.writerows(products)
        
def csv_cmd():
    filename = input("Enter the name of file:   ")
    
    with open(filename, 'r', encoding='utf-8') as file:
        res = csv.DictReader(file, delimiter='|')
        
        for line in res:
            print(line)
                 
def main():
        global id
        while True:
            choice = print_menu()
            match choice:
                case 0:
                    break
                case 1:
                    add_product()
                case 2:
                    view_product(products)
                case 3:
                    result = search_products()
                    if len(result) == 1:
                        print_one_product(result)
                    else:
                        print_many_product(result)
                case 4:
                    edit_Product()
                case 5:
                    delete_product()
                case 6:
                    load_to_txt()
                case 7: 
                    txt_cmd()
                case 8:
                    load_to_json()
                case 9:
                    json_to_cmd()
                case 10:
                    load_csv()
                case 11:
                    csv_cmd()
                case _:
                    print("Enter a valid Choice Given  ")
                    
                    
if __name__ == '__main__':
    main()
        
    