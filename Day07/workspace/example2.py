class Book:
    def __init__(self, title = None, author = None):
        self.title = title
        self.author = author

    def __str__(self):
        """
        This function is expected to return the textual version of the current object
        """
        return f'Book object with title={self.title!r} and author={self.author!r}'

def main():
    b1 = Book('Let us C", "Y Kanitkar')
    b2 = Book('Python made easy, John Doe')
    b3 = Book('Java unreleased')
    b4 = Book()

    print(id(b1))
    print(b1)           # b1.__str__ is called automatically
    print(b2)
    print(b3)
    print(b4)

main()