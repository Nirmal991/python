def main():
    string = input("Enter the string: ")

    if '@' not in string:
        print("String does not contain @")
    else:
        domain = string.split("@")[1]
        print(domain)

main()