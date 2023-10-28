def filter_characters(x=1, strings=None, flag=True):
    if strings is None:
        strings = []
    result = []

    for s in strings:
        filtered_chars = []
        for char in s:
            if (ord(char) % x == 0) if flag else (ord(char) % x != 0):
                filtered_chars.append(char)
        result.append(filtered_chars)

    return result


y = 2
strings_y = ["test", "hello", "lab002"]
flag_y = False
filtered_lists = filter_characters(y, strings_y, flag_y)
print(filtered_lists)
