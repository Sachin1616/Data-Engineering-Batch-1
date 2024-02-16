# Define a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self, miles):
        self.miles_driven += miles
        print(f"The car has been driven {miles} miles.")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Miles Driven: {self.miles_driven}")


# Create an object of the class
my_car = Car("Toyota", "Camry", 2020)

# Call methods on the object
my_car.drive(100)
my_car.drive(50)
my_car.display_info()
