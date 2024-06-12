#13. Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        age = calculate_age(birth_year)
        print("You are", age, "years old.")
    except ValueError:
        print("Please enter a valid year.")

if __name__ == "__main__":
    main()
