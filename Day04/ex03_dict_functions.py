from vinutils import line
from pprint import pprint

line()
p1 = dict(name = "Vinod",
          email = "vinod@gmail.com",
          phones = "9435378363",
          city = "Bangalore",
          title = "Mr.")


for key in p1.keys():
    print(key)

line()

for key in p1:
    print(key)

for value in p1.values():
    print(value)

for kv in p1.items():
    print(kv)

for key, values in p1.items():
    print(f"{key=} and {values=}")

line()

k,v = p1.popitem()
print(f"deleted the key {k} with value {v}")
print(p1)

print(f"{p1.pop("email") = }")


