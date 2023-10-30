def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for key in dict1:
            if not compare_dicts(dict1[key], dict2[key]):
                return False

    elif isinstance(dict1, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False

        for item1, item2 in zip(dict1, dict2):
            if not compare_dicts(item1, item2):
                return False

    else:
        if dict1 != dict2:
            return False

    return True


def main():
    dict1 = {'a': 1, 'b': [1, 2, 3], 'c': {'x': 'hello'}}
    dict2 = {'a': 1, 'b': [1, 2, 3], 'c': {'x': 'hello'}}

    result = compare_dicts(dict1, dict2)
    print(result)


if __name__ == "__main__":
    main()
