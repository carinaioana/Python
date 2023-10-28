def order_tuples(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[1][2])

    return sorted_tuples


input_tuples = [('abc', 'bcd'), ('abc', 'zza')]
sorted_result = order_tuples(input_tuples)
print(sorted_result)
