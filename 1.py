def convert_to_words(number):
    # Define arrays for one-digit and two-digit numbers
    one_digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digit_words = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_words = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    # Convert the number to a string
    num_str = str(number)
    
    # Initialize empty list to store words for each digit
    word_representation = []
    
    # Convert each digit to its word representation
    for digit in num_str:
        word_representation.append(one_digit_words[int(digit)])
    
    # Return the word representation as a string
    return ' + '.join(word_representation)

def count_letters_in_words(N):
    word_representation = convert_to_words(N)
    # Count the total number of letters in the word representation
    total_letters = sum(len(word) for word in word_representation if word.isalpha())
    return total_letters

# Example usage:
number = int(input("Enter a number: "))
total_letters = count_letters_in_words(number)
print("Total number of letters:", total_letters)
