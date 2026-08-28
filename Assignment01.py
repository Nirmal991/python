import math
def main(): 


    """
Exercise 1: Leap Year Checker

Write a program that takes a year as input from the user and checks whether it is a leap year or not.

    Leap Year Criteria: A year is a leap year if it is divisible by 4, except for century years (ending in 00), which must also be divisible by 400.
    Sample Input: 2024
    Sample Output: 2024 is a Leap Year
"""

    def Leap_year():
        year = int(input("Enter a year: "))

        if year < 1:
            print(f"Invalid year: {year}. Year must be a positive integer.")
            return
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")

    # Leap_year()

    """
    Exercise 2: Fibonacci Sequence Generator

Write a Python script to print the first N terms of the Fibonacci sequence, where N is provided by the user.

    Fibonacci sequence: 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , …
    Sample Input: N = 6
    Sample Output: 0, 1, 1, 2, 3, 5

    """
    def Fibonacci_seq():
        N = int(input("Enter the number of terms: "))
        a= 0
        b = 1

        for i in range(N):
            if i<N-1:
                print(a, end=", ")
            else:
                print(a)
            a,b = b, a+b

    # Fibonacci_seq()

    """
    Exercise 3: Prime Number Checker

Write a program that checks whether a positive integer entered by the user is a prime number.

    Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    Sample Input: 17
    Sample Output: 17 is a prime number.
"""

    def Prime_num():
        num = int(input("Enter a number: "))

        if num < 2:
            print(f"{num} is not a Prime number.")
            return

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                return

        print(f"{num} is a prime number.")

    # Prime_num()

    """
    Exercise 4: Odd or Even Checker

Write a program that prompts the user for an integer and prints whether it is even or odd.

    Sample Input: 7
    Sample Output: 7 is an Odd number.
"""

    def Odd_Even():
        num = int(input("Enter a number: "))

        if(num % 2 == 0):
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")

    # Odd_Even()

    
        """
        Exercise 5: Basic Operator Calculator

Create a program that takes two numbers and a math operator (+, -, *, /) from the user, performs the corresponding calculation, and prints the result.

    Sample Input: num1=15, num2=3, operator='/'
    Sample Output: Result: 5.0
"""

    def basic_calc():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator not in ['+', '-', '*', '/']:
            print(f"Invalid operator: {operator}. Please use one of +, -, *, /.")
            return

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}") 
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")
    
    # basic_calc()

    """
    Exercise 6: Sum of N Natural Numbers

Write a script that accepts a positive integer N from the user and calculates the sum of all natural numbers up to N .

    Formula: ∑ i = 1 N i = N ( N + 1 ) 2
    Sample Input: N = 10
    Sample Output: Sum: 55
"""

    def sum_natural():
        num = int(input("Enter a positive integer: "))

        sum = (num * (num + 1)) / 2
        print(f"Sum of first {num} natural numbers is: {int(sum)}")

    # sum_natural()

    """
    Exercise 7: Multiplication Table Generator

Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.

    Sample Input: 5
    Sample Output:

    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
"""

    def multiplication():
        num = int(input("Enter a number: "))
        for i in range(11):
            result = num * i
            print(f"{num} x {i} = {result}")

    # multiplication()

    """
    Exercise 8: Score to Grade Converter

Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
"""
    def grade_generator():
        num = int(input("Enter the number: "))

        if num >= 90 and num <= 100:
            print("A")
        elif num >= 80 and num <= 89:
            print("B")
        elif num >= 70 and num <= 79:
            print("C")
        elif num >= 60 and num <= 69:
            print("D")
        elif num >= 50 and num <= 59:
            print("E")
        elif num >= 40:
            print("F")
    grade_generator()
main()