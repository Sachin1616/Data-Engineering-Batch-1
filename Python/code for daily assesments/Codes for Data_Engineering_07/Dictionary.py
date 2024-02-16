# Creating a dictionary
student = {
    'name': 'Akash',
    'age': 22,
    'grade': 'A+',
    'courses': ['Soft_Skills', 'Technical', 'Data_Engineering']
}

# Accessing values using keys
print("Student Name:", student['name'])
print("Student Age:", student['age'])
print("Student Courses:", student['courses'])

# Modifying values
student['age'] = 21
student['grade'] = 'A'

# Adding a new key-value pair
student['gender'] = 'Male'

# Dictionary after modifications
print("\nUpdated Student Information:")
print("Student Name:", student['name'])
print("Student Age:", student['age'])
print("Student Grade:", student['grade'])
print("Student Gender:", student['gender'])
print("Student Courses:", student['courses'])

# Dictionary methods
print("\nDictionary Methods:")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Removing a key-value pair
removed_course = student.pop('courses')
print("\nRemoved Course:", removed_course)
print("Updated Student Information after removing 'courses' key:", student)
