def name():
    string = input("enter the string: ")
    short_str = ""
    split = string.split()

    for i in range (len(split) - 1):
        short_str += split[i][0] + ". " + " "
        short_str += split[-1]

    print(short_str)