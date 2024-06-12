#18. Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if are_anagrams(string1, string2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

if __name__ == "__main__":
    main()
