def main():
    str = input("Enter a String: ")

    st = str.split()
    print(len(st))


    count = 0
    for i in str:
        count+=1
    # print(count)
    print(f"Total length: {len(str)}")

main()