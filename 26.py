#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def starts_with_prefix(input_string, prefix):
    return input_string.startswith(prefix)

def ends_with_suffix(input_string, suffix):
    return input_string.endswith(suffix)

def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")

    if starts_with_prefix(input_string, prefix):
        print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")

    if ends_with_suffix(input_string, suffix):
        print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")

if __name__ == "__main__":
    main()
