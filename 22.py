#22. Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_and_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

def main():
    input_string = input("Enter a list of numbers, separated by commas: ")
    numbers = list(map(float, input_string.split(',')))
    min_value, max_value = find_min_and_max(numbers)
    print(f"The minimum value is: {min_value}")
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()
