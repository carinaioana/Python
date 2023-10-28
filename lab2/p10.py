def combine_lists(*args):
    # Find the maximum length among all input lists
    max_len = max(len(lst) for lst in args)

    result = []

    for i in range(max_len):
        # Create a tuple containing elements from input lists at the current index
        # If a list is shorter, fill in with None
        combined_tuple = tuple(lst[i] if i < len(lst) else None for lst in args)

        result.append(combined_tuple)

    return result


def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c"]

    r = combine_lists(list1, list2, list3)

    print(r)


if __name__ == "__main__":
    main()
