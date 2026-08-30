# empty_list = []

# numbers = [10, 20, 30, 40]

# mixed_list = ["Alice", 42, 3.14, True, None]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# # Indexing

# fruits = ["apple", "banana", "cherry", "date"]

# # Positive Indexing (Left-to-Right)
# print(fruits[0])   # Output: apple
# print(fruits[2])   # Output: cherry

# # Negative Indexing (Right-to-Left)
# print(fruits[-1])  # Output: date (Last element)
# print(fruits[-3])  # Output: banana

# # Slicing

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[2:6])
# print(numbers[:4])
# print(numbers[5:])
# print(numbers[::2])
# print(numbers[::-1])

# Modifying 

# items = ["phone", "laptop", "tablet"]
# items[1] = "desktop"
# print(items)  # Output: ['phone', 'desktop', 'tablet']

# shopping = ["milk", "bread"]

# # Append
# shopping.append("eggs")
# print(shopping)  # Output: ['milk', 'bread', 'eggs']

# # Insert
# shopping.insert(1, "butter")
# print(shopping)  # Output: ['milk', 'butter', 'bread', 'eggs']

# # Extend
# snacks = ["chips", "cookies"]
# shopping.extend(snacks)
# print(shopping)  # Output: ['milk', 'butter', 'bread', 'eggs', 'chips', 'cookies']

tasks = ["code", "test", "deploy", "test"]
# tasks.remove("test")
# print(tasks)
# tasks.remove("call") ERROR

# popped_item = tasks.pop()
# print(f"Popped item: {popped_item}")
# print(tasks)

# numbers = [10,20,30,40]

# del numbers[::1]
# print(numbers)

# grades = [90, 75, 88, 75, 95]

# print(grades.count(75))  # Output: 2
# print(grades.index(88))  # Output: 2

# # Sort in-place (ascending)
# grades.sort()
# print(grades)  # Output: [75, 75, 88, 90, 95]

# # Sort in-place (descending)
# grades.sort(reverse=True)
# print(grades)  # Output: [95, 90, 88, 75, 75]

# # Reverse in-place
# grades.reverse()
# print(grades)  # Output: [75, 75, 88, 90, 95]

group1 = [1, 2]
group2 = [3, 4]

# group3 = group1 + group2
# print(group3)

group4 = group1 * 2
# print(group4)

colors = ["red", "green", "blue"]

# print("red" in colors)
# print("pink" in colors)

# LIST COMPREHENSION

square = [x ** 2 for x in range(1,6) if x%2 == 0]
print(square)

str_input = ["10", "20", "30", "40", "50"]
integers = [int(num) for num in str_input]
print(integers)

raw_cities = ["  Bangalore ", " MANGALORE", "chennai   ", "Delhi"]
clean = [o.strip().title() for o in raw_cities]
print(clean)

emails = ["vinod@vinod.co", "kishori@acts.in", "student@gmail.com", "admin@vinod.co"]

res = [email for email in emails if email.endswith("@vinod.co")]
print(res)

r = [email for email in emails if email.split('@')[1] == "vinod.co" ]
print(r)

scores = [45, 88, 30, 92, 50]
result = ['Pass' if score > 50 else 'Fail' for score in scores]
print(result)

matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for row in matrix for num in row]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

