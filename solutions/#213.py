def generate_ip(digits):
    return helper("", 3, digits)


def helper(current, left, string):
    if not left:
        current += string
        if not is_valid(current):
            return None
        return [current]
    results = []
    for i in range(1, len(string)):
        pos = helper(current + string[:i] + ".", left - 1, string[i:])
        if pos:
            results.extend(pos)
    return results


def is_valid(ip):
    for sub in ip.split("."):
        if not sub:
            return False
        if len(sub) > 3 or int(sub) < 0 or int(sub) > 255:
            return False
        if len(sub) > 1 and int(sub) == 0:
            return False
        if len(sub) > 1 and int(sub) != 0 and int(sub[0]) == 0:
            return False

    return True


def main():
    assert generate_ip("2542540123") == ['254.25.40.123', '254.254.0.123']


if __name__ == '__main__':
    main()
