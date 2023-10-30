def loop(mapping):
    visited = set()
    result = []

    current_key = "start"

    while current_key not in visited:
        visited.add(current_key)
        result.append(mapping[current_key])
        current_key = mapping[current_key]

    return result


def main():
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    result = loop(mapping)
    print(result)


if __name__ == "__main__":
    main()

