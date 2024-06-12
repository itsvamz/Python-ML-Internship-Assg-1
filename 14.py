#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

def main():
    print("Enter multiple lines of input. Press Enter on an empty line to finish.")
    lines = read_lines()
    print("\nYou entered the following lines:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
