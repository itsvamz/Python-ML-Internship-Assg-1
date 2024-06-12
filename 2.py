#2. Write a python program that checks whether a given number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        number = int(input("Enter a number: "))
        result = check_even_odd(number)
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
