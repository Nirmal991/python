def title_format():
    str = input("Enter a String: ")

    split_str = str.split()

    res = []

    for word in split_str:
        new_word = word[0].upper() + word[1:].lower()
        res.append(new_word)

    print(" ".join(res))

def main():
    title_format()

main()