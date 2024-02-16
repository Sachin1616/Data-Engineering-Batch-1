'''
#Varaibles(A variable is a symbolic name associated with a value or data storage location in computer programming.)
x = "Hello, Python!" # x is a variable storing a string
print(x)

'''
 #Operators

'''
# Arithmetic Operators

# Input values
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition = num1 + num2
print(f"Addition: {num1} + {num2} = {addition}")

# Subtraction
subtraction = num1 - num2
print(f"Subtraction: {num1} - {num2} = {subtraction}")

# Multiplication
multiplication = num1 * num2
print(f"Multiplication: {num1} * {num2} = {multiplication}")

# Division

# Checking if the divisor is not zero
if num2 != 0:
    division = num1 / num2
    print(f"Division: {num1} / {num2} = {division}")
else:
    print("Cannot divide by zero.")

# Modulo
modulo = num1 % num2
print(f"Modulo: {num1} % {num2} = {modulo}")

# Exponentiation
exponentiation = num1 ** num2
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")

# Floor Division
# Checking if the divisor is not zero
if num2 != 0:
    floor_division = num1 // num2
    print(f"Floor Division: {num1} // {num2} = {floor_division}")
else:
    print("Cannot perform floor division by zero.")
'''

# Comparison Operators
'''
# Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Using Comparison Operators
is_equal = num1 == num2
not_equal = num1 != num2
greater_than = num1 > num2
less_than = num1 < num2
greater_than_or_equal = num1 >= num2
less_than_or_equal = num1 <= num2

# Displaying results
print(f"\nComparison Results for {num1} and {num2}:")
print(f"Is Equal: {is_equal}")
print(f"Not Equal: {not_equal}")
print(f"Greater Than: {greater_than}")
print(f"Less Than: {less_than}")
print(f"Greater Than or Equal: {greater_than_or_equal}")
print(f"Less Than or Equal: {less_than_or_equal}")
'''

# Logical Operators Program
'''
# Input values
x = True
y = False

# Logical AND
result_and = x and y

# Logical OR
result_or = x or y

# Logical NOT
result_not_x = not x
result_not_y = not y

# Displaying results
print("Input values:")
print("x =", x)
print("y =", y)

print("\nLogical AND:")
print("x and y =", result_and)

print("\nLogical OR:")
print("x or y =", result_or)

print("\nLogical NOT:")
print("not x =", result_not_x)
print("not y =", result_not_y)
'''

# Bitwise Operators
'''
num1 = 5  # Binary: 0b101
num2 = 3  # Binary: 0b011

bitwise_and = num1 & num2  # Binary: 0b001 (1 in decimal)
bitwise_or = num1 | num2   # Binary: 0b111 (7 in decimal)
bitwise_xor = num1 ^ num2  # Binary: 0b110 (6 in decimal)
bitwise_not_num1 = ~num1   # Binary: 0b...11111111111111111111111111111010 (Two's complement representation)
left_shift = num1 << 2     # Binary: 0b10100 (20 in decimal)
right_shift = num1 >> 1    # Binary: 0b10 (2 in decimal)

# Displaying results
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT (num1):", bitwise_not_num1)
print("Left Shift (num1):", left_shift)
print("Right Shift (num1):", right_shift)
'''

# Identity Operators
'''
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# "is" and "is not" identity operators
are_objects_equal = (a is b)
are_objects_not_equal = (a is not b)
are_objects_c_equal = (a is c)

# Displaying results
print("Identity Operators:")
print("Are objects 'a' and 'b' equal?", are_objects_equal)
print("Are objects 'a' and 'b' not equal?", are_objects_not_equal)
print("Are objects 'a' and 'c' equal?", are_objects_c_equal)
'''