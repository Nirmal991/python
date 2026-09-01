from random import randrange
from itertools import groupby
def main():
    # nums = [randrange(5000) for _ in range(10)]
    # print(nums)

    # even = [num for num in nums if num%2 == 0]

    # odd = [num for num in nums if num %2 != 0]

    # print()
    # print(f"{even=}")
    # print(f"{odd=}")
    # # print(f"odd=")

    ...
    multiply = lambda x,y: x*y
    print(multiply(3,4))

    num = [1,2,3,4,5]
    sq = list(map(lambda x: x**2, num))
    print(sq)

    num = [1,2,3,4,5,6]

    fil = list(filter(lambda x : x % 2 == 0, num))

    print(fil)

    fruits = ["apple", "banana", "orange", "mango", "kiwi", "pineapple"]
    # res = sorted(fruits, key= lambda x: len(x))
    # print(res)

    groups = groupby(sorted(fruits), key=lambda x : x[0])
    for key, group in groups:
        print(key, list(group))



main()