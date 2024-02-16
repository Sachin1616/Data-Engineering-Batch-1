# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Adding elements to a set
set1.add(6)
print("After adding 6 to set1:", set1)

# Removing elements from a set
set2.remove(7)
print("After removing 7 from set2:", set2)

# Union of sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference between sets
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)

# Check if a set is a subset of another set
subset_check = {3, 4}.issubset(set1)
print("{3, 4} is a subset of set1:", subset_check)
