# import pickle

# # student = {
# #     "name": "Nirmal",
# #     "age": 25,
# #     "marks": [80, 85, 90]
# # }

# # # Save object
# # with open("student.pkl", "wb") as file:
# #     pickle.dump(student, file)

# with open("student.pkl", "rb") as file:
#     student = pickle.load(file)

# print(student)

import pickle

class ProductCatalog:
    def __init__(self, category):
        self.category = category
        self.items = []

    def add_product(self, name, price):
        self.items.append({"name": name, "price": price})

catalog = ProductCatalog("Beverages")
catalog.add_product("Chai", 18.0)

# Save live class instance to binary file (dump)
with open("catalog.pkl", "wb") as f:
    pickle.dump(catalog, f)

# Restore live class instance from binary file (load)
with open("catalog.pkl", "rb") as f:
    restored_catalog = pickle.load(f)

print(f"Restored Category: {restored_catalog.category} | Items: {restored_catalog.items}")