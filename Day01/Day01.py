# print("Hello, World!")

# a = 10
# b = 3.5
# c = 1 + 2j


# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'float'>
# print(type(c))

# print(type(a).__name__)

# x = y = z = 100
# print(x, y, z)


# name = "Nirmal"
# age = 22
# print("Name: ", name, "Age: ", age)
# print("24", "08", "209", sep = "-")
# help(sep())

# print("Hello", end=" ")
# print("World")  # Output: Hello World (on the same line)

# a = 'Nirmal'
# b = 32

# print("Name: "+ a +  " Age: " + str(b))
# print("Name: {} Age: {}".format(a, b))
# print(f"Name: {a}  Age: {b}")

# age = 22

# print(f"Status: {'Adult' if age >= 18 else 'Miniom'}")

# a = 10
# b = 20
# print(f"Sum:  {a+b}")

def main(): 
    # name, city = 'Vinod', 'Bangalore'
    # temp = 22

    # print(f'{name=}')
    # print(f'{city=}')
    # print(f'{temp=}')

    # print(name)
    # print(city)
    # print(temp)

    # name = input("Enter your name: ")
    # city = input("Enter your city: ")

    # if name.strip() == "":
    #     name = "Unknown"
    
    # if len(city.strip()) == 0:
    #     city = "your city"

    # print(f"Hello { name}, how's {city}?")

    # year = int(input("Enter a year: "))
    # month = int(input("Enter a month (1-12): "))

    # if year < 1: 
    #     print(f"Invalid year: {year}. Year must be a positive integer.")
    #     # exit(1)
    #     return
    # if month < 1 or month > 12:
    #     print(f"Invalid month: {month}. Month must be between 1 and 12.")
    #     return

    # if month == 2:
    #     max_days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28

    # elif month in (4, 6, 9, 11):
    #     max_days = 30
    # else: 
    #     max_days = 31

    # print(f"{month}/{year} has {max_days} days")

    """
This is an example script to understand the use of `while` loop.

Accept a number from the user and check if it is a prime or not.
"""

    # num = int(input("Enter a number: "))

    # if num < 0:
    #     print(f"{num} enter a positive number.")
    #     continue

    # break

    # limit = num // 2
    # d == 2

    # while d <= limit:
    #     if num % d ==0:
    #         print(f"{num} is not a prime number.")
    #         break
    #     d += 1
    # else: 
    #     print(f"{num} is a prime number.")


"""
Example of a `for` loop.

Accept two numbers from the user, and print all prime numbers between them.
"""

    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))

    if start > end:
        print("first number must be smaller than the second number.")
        return

    for n in range(start, end+1):
        limit = n // 2
        for d in range(2, limit+1):
            if n % d == 0:
                break
        else:
            print(n, end=", ")
main()

