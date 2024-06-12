#16. Write a program in python that counts the frequency of each character in a string 
def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    input_string = input("Enter a string: ")
    character_frequency = count_character_frequency(input_string)
    print("Character frequencies:")
    for char, freq in character_frequency.items():
        print(f"{char}: {freq}")

if __name__ == "__main__":
    main()
