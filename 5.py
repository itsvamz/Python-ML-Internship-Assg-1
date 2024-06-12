#5. Write a program that takes a string input from the user and writes it to a text file.
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote the content to '{filename}'.")
    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")

def main():
    content = input("Enter the content to write to the file: ")
    filename = input("Enter the filename to write to (include extension, e.g., 'output.txt'): ")
    write_to_file(filename, content)

if __name__ == "__main__":
    main()
