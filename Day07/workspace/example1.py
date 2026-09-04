class Book():
    def __init__(self):
        self.title = "Let us C"
        self.author = "Y kanitkar"
        print('Book object insatantiated!')

def main():
    b1 = Book()
    b2 = Book()

    print(f'{id(b1) = }')
    print(f'{type(b1) = }')
    print(f'{dir(b1) = }')

main()