
def count_words(txt):
    # Split the text into words using space as a delimiter
    words = txt.split()
    return len(words)


user_input = input("Enter a text: ")


word_count = count_words(user_input)


print("The number of words in the text is:", word_count)