def is_palindrome(num):
    return str(num) == str(num)[::-1]


def count_and_find_largest_palindrome(numbers):
    count = 0
    largest_palindrome = None

    for num in numbers:
        if is_palindrome(num):
            count += 1
            # Update the largest palindrome if needed
            if largest_palindrome is None or num > largest_palindrome:
                largest_palindrome = num

    return count, largest_palindrome


number_list = [121, 12321, 456, 78987, 54345, 123]
result = count_and_find_largest_palindrome(number_list)
print(result)
