
def is_palindrome_number(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the string is the same as its reverse
    return number_str == number_str[::-1]


user_input = input("Enter a number: ")

print("The number is a palindrome:", is_palindrome_number(user_input))
