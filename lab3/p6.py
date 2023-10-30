def count_unique_duplicates(l):
    unique = set()
    duplicates = set()
    for i in l:
        if l.count(i) == 1:
            unique.add(i)
        if l.count(i) > 1:
            duplicates.add(i)
    return len(unique), len(duplicates)


def main():
    my_list = [1, 2, 2, 3, 4, 4, 5]
    result = count_unique_duplicates(my_list)
    print(result)


if __name__ == "__main__":
    main()
