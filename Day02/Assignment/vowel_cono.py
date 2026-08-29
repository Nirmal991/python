def freq():
    str = input("Enter a String: ")
    cA = 0
    cE = 0
    cI = 0
    cO = 0
    cU = 0
    cC = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for ch in str:
        if ch == 'a':
            cA+=1
        elif ch == 'e':
            cE +=1
        elif ch == 'i':
            cI += 1
        elif ch == 'o':
            cO += 1
        elif ch == 'u':
            cU += 1
        elif ch.isalpha():
                cC+=1

    print(f"vowel Frequencies: ")
    print(f"a: {cA}")
    print(f"e: {cE}")
    print(f"i: {cI}")
    print(f"o: {cO}")
    print(f"u: {cU}")
    print(f"Total Consonants: {cC}")

def main(): 
     freq()

main()
            
