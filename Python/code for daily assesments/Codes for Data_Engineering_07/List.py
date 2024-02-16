# Creating a list
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

#List Methods
# 1 append(): Adds an element to the end of the list.
fruits.append("mango")
print("List after adding 'mango':", fruits)

# 2 insert(): Inserts an element at a specified position in the list.
fruits.insert(1, "kiwi")
print("List after inserting 'kiwi' at index 1:", fruits)

# 3 remove(): Removes the first occurrence of a specified element from the list.
fruits.remove("apple")
print("List after removing 'apple':", fruits)

# 4 pop(): Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.
popped_element = fruits.pop(2)
print("List after popping element at index 2:", fruits)
print("Popped element:", popped_element)

# 5 clear(): Removes all elements from the list.
fruits.clear()
print("List after clearing:", fruits)

# 6 List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice from index 2 to 5 (exclusive)
slice_result = numbers[2:5]
print("Slice from index 2 to 5:", slice_result)

# Slice from the beginning to index 4 (exclusive)
slice_result = numbers[:4]
print("Slice from the beginning to index 4:", slice_result)

# Slice from index 5 to the end
slice_result = numbers[5:]
print("Slice from index 5 to the end:", slice_result)

# Slice with a step of 2
slice_result = numbers[1:8:2]
print("Slice with a step of 2:", slice_result)
