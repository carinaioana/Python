def set_operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            union_key = f"{set1} | {set2}"
            result[union_key] = set1 | set2

            intersection_key = f"{set1} & {set2}"
            result[intersection_key] = set1 & set2

            difference_ab_key = f"{set1} - {set2}"
            result[difference_ab_key] = set1 - set2

            difference_ba_key = f"{set2} - {set1}"
            result[difference_ba_key] = set2 - set1

    return result


def main():
    set1 = {1, 2}
    set2 = {2, 3}
    result_dict = set_operations(set1, set2)

    for key, value in result_dict.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
