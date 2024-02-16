# Define a function to double a number
def double(x):
    return x * 2

# Using map() to apply the double function to each element of a list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)

# Convert the map object to a list and print the result
print("Doubled numbers:", list(doubled_numbers))
