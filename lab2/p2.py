def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def find_prime(numbers):
    prime_numbers = []
    for n in numbers:
        if is_prime(n):
            prime_numbers.append(n)
    return prime_numbers


def main():
    numbers_list = [2, 3, 5, 7, 8, 11, 13, 17, 19, 20]
    print(find_prime(numbers_list))


if __name__ == "__main__":
    main()
