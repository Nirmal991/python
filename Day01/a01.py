# question1 
import math
def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print("Not a leap year")
        
# leap_year(1900)

# quest 2

def fibonachi(num):
    a = 0
    b = 1
    for i in range(num):
        print(a)
        a,b = b,a+b
    
    
# fibonachi(6)

# quest 3
def prime_checker(num):
    if num < 2:
        print(f"{num} is not a prime number")
        return

    sqrt = math.isqrt(num)

    for i in range(2, sqrt + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return

    print(f"{num} is a prime number")

# prime_checker(10)

#  ques 4

def odd_even(num):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is a odd number")
        
# quest 5

def calc(num1, num2, str):
    match str:
        case '+':
            print(num1 + num2)
        case '-':
            print(num1 - num2)
        case '*':
            print(num1*num2)
        case '/':
            print(num1/num2)
        case _:
            print("Enter a valid operator")
            
            
calc(10, 20, '/')

# ques 6

def sum_of_natural(num):
    sum = (num * (num+1)/2)
    print(sum)
    
def table(num):
    for i in range(1, 11):
        mul = i*num
        print(f"{num} x {i} = {mul}")
        
table(5)