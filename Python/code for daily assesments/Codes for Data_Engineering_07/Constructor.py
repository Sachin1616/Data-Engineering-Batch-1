class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and calling methods
person1.introduce()
person2.introduce()
