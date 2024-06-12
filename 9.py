#9. Write a python program that checks if a substring is present in a given string.
a = input("Enter the main string: ")
sub = input("Enter the substring: ")
if sub in a:
    print("Yes, its a substring.")
else:
    print("No, its not a substring.")