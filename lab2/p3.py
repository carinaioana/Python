def list_operations(a, b):
    intersection = []
    union = a.copy()
    a_not_in_b = []
    b_not_in_a = []

    for item in a:
        if item in b:
            intersection.append(item)
        if item not in b:
            a_not_in_b.append(item)

    for item in b:
        if item not in union:
            union.append(item)
        if item not in a:
            b_not_in_a.append(item)

    return intersection, union, a_not_in_b, b_not_in_a


def main():
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]

    result = list_operations(list_a, list_b)
    print("List a:", list_a)
    print("List b:", list_b)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("A - B:", result[2])
    print("B - A:", result[3])


if __name__ == "__main__":
    main()
