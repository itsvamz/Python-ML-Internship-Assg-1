#15. Write a program that reads data from a CSV file and prints it to the console.
import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found.")

def main():
    filename = input("Enter the CSV file name: ")
    read_csv_file(filename)

if __name__ == "__main__":
    main()
