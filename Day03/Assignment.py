def wizzard(): 
    portion = ["staff", "potion", "spellbook"]

    _input = input("Enter the string: ")
    poppped = portion.pop(0)
    portion.append(_input)

    print("Portal transition activated!")
    print(f"Ejected oldest item: {poppped}")
    print(f"Current items in the magic bag: {portion}")

def movie():
    playlist = ["Inception", "The Matrix", "Interstellar"]

    song = input("Enter the song: ")

    if song in playlist:
        print("Already Added!")
    else:
        playlist.append(song)
        sorted_List = sorted(playlist, key = lambda x: x.lower())

    print(sorted_List)

def cargo():
    resources = ["coal", "iron", "gold", "coal", "timber", "coal"]

    ires = input("Enter the res: ")

    if ires in resources:
        print(f"Number of {ires} wagons: {resources.count(ires)}")
        print(f"First {ires} wagon is at index: {resources.index(ires)}")
    else:
        print(f"{ires} not foun din list")

    def vip():
        l = ["Guido", "Esha", "Rajan", "Kishori"]
        guest = input("Enter the users: ")
        while True:
            if l.count(guest):
                l.pop(l.index(guest))
                l.insert(0, guest)  
                print(f"{guest} moved to the front!")
            elif guest == "exit":
                break
            else: 
                print("Access denied. Not on the VIP list.")
        print(f"Current VIP queue: {l}")

def spy():
    s = input("Enter the string: ")
    split_s = s.split()
    res = " ".join([i[::-1] for i in split_s])
    print(res)

def marks():
    inp_strn = input()

    res = [
        min(100, int(marks) + (10 if int(marks) < 50 else 5))
        for marks in inp_strn.split()
    ]

    print(res)

def treasure():
    cordinates = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    res = [cord for cord in cordinates if cordinates[0] > 0 and cordinates[1] > 0]

def cart():
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    op = list({items for items in cart})
    print(f'{op = }')
    

def main():
    # wizzard()
    # movie()
    # cargo()
    # spy()
    cart()
    ...

main()