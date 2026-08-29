def cipher():
    string = input("Enter a String: ")
    res = ""
    for ch in string:
        if ch.isupper():
            res+= chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
        elif ch.islower():
            res+= chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
        else:
            res += ch

    print(res)

def main():
    cipher()

main()