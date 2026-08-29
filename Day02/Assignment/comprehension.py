def comp():
    str = input()
    count = 1
    res = ""

    for i in range (len(str)):
        if i == len(str) - 1:
            res += str[i] + str(count)
        elif str[i] == str[i+1]:
            count+=1
        else:
            res += str[i] + str(count)
            count = 1

        if len(res.split('1') - 1 == len(str)):
            res = str
    print(res)