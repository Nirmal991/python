from random import randrange

def main():
    nums = [randrange(5000) for _ in range(10)]
    print(nums)

    even = [num for num in nums if num%2 == 0]

    odd = [num for num in nums if num %2 != 0]

    print()
    print(f"{even=}")
    print(f"{odd=}")
    # print(f"odd=")
main()