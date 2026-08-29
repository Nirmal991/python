# Strings

messages = "Hello World! "
age = 25
# print(type(age))
age_str = str(age)
# print(type(age_str))


original = "Python"
# print(id(original))  # E.g., 4381982704

# Modifying the string
modified = original + " 3"
# print(id(modified))  # E.g., 4381983584 (a completely new address!)
# print(original)      # Still prints "Python"

text = "PYTHON"
# print(text[0])  # Output: 'P' (First character)
# print(text[2])  # Output: 'T' (Third character)
# print(text[5])  # Output: 'N' (Last character)

# print(text[-1]) # Output: 'N' (Last character)
# print(text[-2]) # Output: 'O' (Second-to-last character)
# print(text[-6]) # Output: 'P' (First character)

# String Concatenation

first_name = "Nirmal"
last_name = "Shrivastava"

fullname = first_name + " " + last_name

age = 35
# print("Age: " + age)  # TypeError: can only concatenate str (not "int") to str

# Fix by casting
# print("Age: " + str(age))  # Output: Age: 35

name = "Rajan"
age = 24
result = "Name: %s, Age: %d" % (name, age)
# print(result)  # Output: Name: Rajan, Age: 24

name = "Vinod Kumar"
city = "Bangalore"

# print(f"name={name}, city={city}")
# print(f"{name=}, {city=}")

# print(f"{city:<15}")
# print(f"{city:>15}")
# print(f"[{city:^15}]")

# print(f"{city:*^15}")

# import datetime
# today = datetime.date(2026, 8, 26)
# print(f"Date: {today: %B %d, %Y}")

# Case conversion

name = "Vinod Kumar Kayartaya"

# print(name.upper())  # Output: VINOD KUMAR KAYARTAYA
# print(name.lower())  # Output: vinod kumar kayartaya
# print(name.title()) # Output: Vinod Kumar

# email = "   vinod@vinod.co   "

# print(f"[{email}]")          # Output: [   vinod@vinod.co   ]
# print(f"[{email.strip()}]")  # Output: [vinod@vinod.co]

# name = "Vinod Kumar Kayartaya"
# # Split the string by spaces into a list
# name_parts = name.split()
# print(name_parts)  # Output: ['Vinod', 'Kumar', 'Kayartaya']

# # Join the list parts back using a dash '-'
# joined_name = "-".join(name_parts)
# print(joined_name)  # Output: Vinod-Kumar-Kayartaya

# # Tuples
# numbers = (1,2,3)

# shorthand_tuple = "Vinod", "Bangalore", 560001
# print(type(shorthand_tuple))  # Output: <class 'tuple'>

# # A tuple containing heterogeneous (mixed) data types
# profile = ("Vinod", 25, "Bangalore", True)

# # Nested tuples
# nested_tuple = ((1, 2), ("a", "b"))

city_coords = ("Bangalore", 12.97, 77.59)
# print(city_coords[0])  
# print(city_coords[-1]) 
# sub_tuple = city_coords[1:3]
# print(sub_tuple)

t1 = (1, 2)
t2 = (3, 4)

# Concatenation
t3 = t1 + t2
# print(t3)  # Output: (1, 2, 3, 4)

# Repetition
t4 = t1 * 3
# t5 = t1 * t2 ERROR
# print(t4)  # Output: (1, 2, 1, 2, 1, 2)

# Tuple Packing and Unpacking

# Packing values
address = ("vinod@vinod.co", "Bangalore", 560001)

email, city, pincode = address
# print(email)
# print(city)

numbers = (1,2,3,4,5,6)

first, *middle, end = numbers
# print(first)
# print(middle)
# print(end)

# Swappig Vaeribles
a = "Vinod"
b = "Bangalore"

# Swap values
a, b = b, a
# print(a)  # Output: Bangalore
# print(b)  # Output: Vinod

# def main():

#     name = "Nirmal"
#     city = "Banglore"
#     address = f"""Centreo,

# {city}"""

#     print(name)
#     print(address)

# print("="*80)

def main(): 
    txt = 'vinod bangalore vinay hassan vinod chennai bangalore chennai bangalore bangalore'

    word = input("Enter a word : ")

    j = 0
    while True:
        i = txt.find(word, j)
        if i == -1:
            break

        print(f'`{word} found in given txt at index {i}`')
        j = i+1

    if j == 0:
        print(f'`{word}` is not found in the given text')

main()

