25. #Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        
        print(f"Contents copied from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except IOError as e:
        print(f"Error: {e}")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
