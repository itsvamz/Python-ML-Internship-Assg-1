#19. Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

def main():
    input_string = input("Enter a string: ")
    no_punctuation_string = remove_punctuation(input_string)
    print("String without punctuation:", no_punctuation_string)
    
if __name__ == "__main__":
    main()
