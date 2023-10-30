def build_xml_element(tag, content, **elements):
    string = " "
    string += '<' + tag + ' '
    for key, value in elements.items():
        string += key + '=\\"' + value + '\\"'
    string += '>'
    string += content
    string += '</' + tag + '>'
    return string


def main():
    result = build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
    print(result)


if __name__ == "__main__":
    main()
