import re


def convert_to_lower_with_underscores(string):
    #  regular expression to split into words
    words = re.findall(r'[A-Z][a-z]*', string)

    # Join the words with underscores and convert to lowercase
    result = '_'.join(words).lower()

    return result


input_string = "UpperCamelCaseExample"
output_string = convert_to_lower_with_underscores(input_string)
print(output_string)
