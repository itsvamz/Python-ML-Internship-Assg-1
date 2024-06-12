#6. Write a program that reads the content of a text file and prints it to the console.
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")

def main():
    filename = input("Enter the filename to read from: ")
    read_file(filename)

if __name__ == "__main__":
    main()
