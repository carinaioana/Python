from collections import Counter


def find_items(x, *lists):
    combined_list = []
    for sublist in lists:
        for item in sublist:
            combined_list.append(item)

    item_counts = Counter(combined_list)

    print(type (item_counts))

    result = []
    for item, count in item_counts.items():
        if count == x:
            result.append(item)

    return result


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
y = 2

r = find_items(y, list1, list2, list3, list4)
print(r)
