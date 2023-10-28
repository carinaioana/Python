import re


def extract_number_from_text(text):
    #  regular expression to find the first number in the text
    match = re.search(r'\d+', text)

    if match:
        # Extract the matched number as a string and convert it to an integer
        number = int(match.group())
        return number
    else:
        return None


text1 = "An apple is 123 USD 33"
text2 = "abc123abc"

number1 = extract_number_from_text(text1)
number2 = extract_number_from_text(text2)

print("Number from text1:", number1)
print("Number from text2:", number2)
