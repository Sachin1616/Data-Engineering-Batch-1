def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type!")
    else:
        print("Result:", result)
    finally:
        print("Exiting divide function.")

# Example usage:
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    divide(num1, num2)
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Exiting program.")
