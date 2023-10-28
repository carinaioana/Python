
def most_common_letter(s):
    # Convert to lowercase to ignore casing
    s = s.lower()

    # dictionary
    letter_count = {}

    for char in s:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Find the letter with the highest count
    most_common = max(letter_count, key=letter_count.get)

    return most_common


input_string = "an apple is not a tomato"
result = most_common_letter(input_string)
print(f"The most common letter is '{result}'")