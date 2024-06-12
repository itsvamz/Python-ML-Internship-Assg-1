#20. Write a python program that takes a list of numbers and returns their sum.
def sum_of_numbers(numbers):
    return sum(numbers)

def main():
    input_string = input("Enter a list of numbers, separated by commas: ")
    numbers = list(map(float, input_string.split(',')))
    total_sum = sum_of_numbers(numbers)
    print("The sum of the numbers is:", total_sum)

if __name__ == "__main__":
    main()
