def validate_dict(rules, data):
    for key, prefix, middle, suffix in rules:
        if key in data:
            value = data[key]
            if not (value.startswith(prefix)
                    and value.endswith(suffix)
                    and middle in value[1:-1]):
                return False
        else:
            return False
    return True


def main():
    rules = {("key1", "", "inside", ""),
             ("key2", "start", "middle", "winter")}
    d = {"key1": "come inside, it's too cold out",
         "key3": "this is not valid"}

    result = validate_dict(rules, d)
    print(result)


if __name__ == "__main__":
    main()
