#7. Write a python program that takes a string as input and returns its length.
def calculate_length(input_string):
    return len(input_string)

def main():
    input_string = input("Enter a string: ")
    length = calculate_length(input_string)
    print(f"The length of '{input_string}' is: {length}")

if __name__ == "__main__":
    main()
