#8. Write a python program that concatenates two strings and returns the result
def concatenate_strings(str1, str2):
    return str1 + str2

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    concatenated_string = concatenate_strings(string1, string2)
    print("Concatenated string:", concatenated_string)

if __name__ == "__main__":
    main()
