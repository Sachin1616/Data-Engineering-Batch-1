class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def make_animal_speak(animal):
    return animal.speak()

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Using polymorphism to make each animal speak
print(make_animal_speak(dog))
print(make_animal_speak(cat))
print(make_animal_speak(cow))  
