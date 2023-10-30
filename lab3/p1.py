def operations(a, b):
    intersection = a & b
    union = a.union(b)
    difference_a_b = a.difference(b)
    difference_b_a = b - a

    return intersection, union, difference_a_b, difference_b_a


def main():
    x = {1, 2, 3, 4}
    y = {2, 3, 4, 5}
    result = operations(x, y)
    print("List x:", x)
    print("List y:", y)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("A - B:", result[2])
    print("B - A:", result[3])


if __name__ == "__main__":
    main()
