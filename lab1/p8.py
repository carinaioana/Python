def count_set_bits(num):
    # store the count of set bits
    count = 0

    while num:
        # bitwise AND to check the least significant bit. 1 => increment the count
        count += num & 1

        # Right shift the number to check the next bit
        num >>= 1

    return count


number = 24
bit_count = count_set_bits(number)
print(f"Number of set bits in {number}: {bit_count}")