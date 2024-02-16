def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the function with different number of arguments
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))
print(sum_all(5, 10, 15, 20, 25))
