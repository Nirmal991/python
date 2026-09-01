from vinutils import line
from pprint import pprint

line()

p1 = dict(name = "Nirmal", email = "nirmal@gmail.com", phones = [9340226247])

print(p1["name"])
print(p1["email"])
print(p1["phones"])

p1["city"] = "Bangalore"
p1["email"] = "nirmal24@gmail.com"
print(f"{p1=}")
print(f'{p1.get('city') = }')