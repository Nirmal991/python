class CA:
    def __init__(self, name):
        self.name = name
        self.is_open = False
        print(f"Object created: {self.name}")

    def fun(self, value):
        if not self.is_open:
            raise RuntimeError("Resource not opened")

        print(f"Processing Value: {value}")

        result = value * 2

        print(f"Result: {result}")

        return result

    def __enter__(self):
        print("Entering...")

        self.is_open = True

        print(f"Resource '{self.name}' opened")

        return self

    def __exit__(self, exc_type, exc, tb):
        print("\nExecuting...")

        if exc_type is not None:
            print(f"Exception Type: {exc_type.__name__}")
            print(f"Exception     : {exc}")
            print("An error occurred inside the with block")
        else:
            print("No exception occurred")

        self.is_open = False

        print(f"Resource '{self.name}' is closed")

        return False


obj1 = CA("MyResource")

with obj1 as resource:
    resource.fun(10)
    resource.fun(20)