#12. Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
number = int(input("Enter a number: "))
print("Sum of the digits:", sum_of_digits(number))
