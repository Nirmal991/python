def com():
    str1 = input()
    count = 1
    res = ""

    for i in range (len(str1)):
        if i == len(str1) - 1:
            res+= str1[i] + str(count)

        elif str1[i] == str1[i+1]:
            count += 1
        else:
            res += str1[i] + str(count)
            count = 1

    if(len(str1) == len(res.split("1")) - 1):
        res = str1

    print(res)

def main():
    com()

main()