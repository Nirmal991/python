def amalgum():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    groups = {}

    for word in words:
        key = "".join(sorted(word))
        print(f"{key=}")

        if key not in groups:
            groups[key] = []
            print(f'{groups=}')

        groups[key].append(word)
        print(f"{groups=}")

    print(list(groups.values()))

def main():
    amalgum()

main()