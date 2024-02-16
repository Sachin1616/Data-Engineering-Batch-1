# Function to read from a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("Contents of the file:")
            print(data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Function to write to a file
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Data written to '{filename}' successfully.")

# Function to append to a file
def append_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
    print(f"Data appended to '{filename}' successfully.")

# Main function
def main():
    filename = "sample.txt"
    content = "This is some sample text.\n"

    # Writing to the file
    write_file(filename, content)

    # Reading from the file
    read_file(filename)

    # Appending to the file
    append_file(filename, "Appending some more text.\n")

    # Reading from the file again
    read_file(filename)

# Entry point of the program
if __name__ == "__main__":
    main()
