def my_function(*args, **kwargs):
    values_set = set(kwargs.values())
    count = 0

    for arg in args:
        if arg in values_set:
            count += 1

    return count


def main():
    result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(result)


if __name__ == "__main__":
    main()
