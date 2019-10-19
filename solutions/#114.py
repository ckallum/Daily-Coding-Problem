import re


def reverse(string):
    delimiter_queue = [(index, delimiter) for index, delimiter in enumerate(string) if not delimiter.isalpha()]
    current = ""
    index = 0
    d_queue = []
    string = [x for x in reversed(re.sub(r'\W+', ' ', string).split())]
    result = []
    while index < len(delimiter_queue):
        current += delimiter_queue[index][1]
        if index + 1 < len(delimiter_queue):
            if not delimiter_queue[index][0] == delimiter_queue[index + 1][0] - 1:
                d_queue.append(current)
                current = ""
        else:
            d_queue.append(current)
        index += 1
    while string:
        current = string.pop(0)
        d = ""
        if d_queue:
            d = d_queue.pop(0)
        result.append(current + d)
    if d_queue:
        result.append(d_queue.pop())
    return "".join(result)


def main():
    assert reverse("hello/world:here") == "here/world:hello"
    assert reverse("hello/world:here/") == "here/world:hello/"
    assert reverse("hello//world:here") == "here//world:hello"


if __name__ == '__main__':
    main()
