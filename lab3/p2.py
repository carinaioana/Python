def occurrences(s):
    d = {}
    for i in s:
        n = s.count(i)
        d[i] = n
    return d


def main():
    example = "Ana has apples"
    print(occurrences(example))


if __name__ == "__main__":
    main()
