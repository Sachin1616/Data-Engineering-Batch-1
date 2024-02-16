def string_operations(input_string):
    # 1. Length of the string
    length = len(input_string)
    print(f"1. Length of the string: {length}")

    # 2. Concatenation
    concatenated_string = input_string + " is awesome!"
    print(f"2. Concatenated string: {concatenated_string}")

    # 3. Substring
    substring = input_string[2:6]
    print(f"3. Substring (index 2 to 5): {substring}")

    # 4. Search
    search_result = input_string.find("Python")
    if search_result != -1:
        print(f"4. 'Python' found at index {search_result}")
    else:
        print("4. 'Python' not found in the string")

    # 5. Replace
    replaced_string = input_string.replace("Python", "Programming")
    print(f"5. String after replacement: {replaced_string}")

    # 6. Convert Case
    uppercase_string = input_string.upper()
    lowercase_string = input_string.lower()
    print(f"6. Uppercase: {uppercase_string}\n   Lowercase: {lowercase_string}")

    # 7. Trim
    trimmed_string = input_string.strip()
    print(f"7. Trimmed string: '{trimmed_string}'")


# Example usage:
user_input = input("Enter a string: ")
string_operations(user_input)
