class MyClass:
    def __init__(self):
        # Public attribute
        self.public_attribute = "I am a public attribute"

        # Protected attribute (convention: prefix with underscore)
        self._protected_attribute = "I am a protected attribute"

        # Private attribute (convention: double underscore prefix)
        self.__private_attribute = "I am a private attribute"

    # Public method
    def public_method(self):
        print("This is a public method")
        self.__private_method()

    # Protected method (convention: prefix with underscore)
    def _protected_method(self):
        print("This is a protected method")

    # Private method (convention: double underscore prefix)
    def __private_method(self):
        print("This is a private method")


# Creating an instance of MyClass
obj = MyClass()

# Accessing public attributes and calling public methods
print(obj.public_attribute)
obj.public_method()
