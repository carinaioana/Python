def fibonacci(nr):
    fibonacci_list = []
    a = 0
    b = 1

    for _ in range(nr):
        fibonacci_list.append(a)
        c = a + b
        a = b
        b = c

    return fibonacci_list


def main():
    n = 10
    print(fibonacci(n))


if __name__ == "__main__":
    main()
