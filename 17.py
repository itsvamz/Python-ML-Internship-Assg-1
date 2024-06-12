#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
def to_title_case(input_string):
    return input_string.title()

def main():
    input_string = input("Enter a string: ")
    title_case_string = to_title_case(input_string)
    print("Title case:", title_case_string)

if __name__ == "__main__":
    main()
