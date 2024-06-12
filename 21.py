#21. Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(elements, target):
    return elements.count(target)

def main():
    input_string = input("Enter a list of elements, separated by commas: ")
    target = input("Enter the element to count: ")
    
    elements = input_string.split(',')
    occurrences = count_occurrences(elements, target)
    
    print(f"The element '{target}' occurs {occurrences} times in the list.")

if __name__ == "__main__":
    main()
