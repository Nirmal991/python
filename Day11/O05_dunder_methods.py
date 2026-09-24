class Demo:

    def __new__(cls):
        print("1. __new__")
        return super().__new__(cls)

    def __init__(self):
        print("2. __init__")

    def __enter__(self):
        print("3. __enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("5. __exit__")

    def __call__(self):
        print("6. __call__")


d = Demo()

with d:
    print("4. Inside with")
    d()