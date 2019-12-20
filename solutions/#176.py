def character_mapping(s1, s2):
    s1_to_s2 = set()
    s2_to_s1 = set()
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if (s1[i] in s1_to_s2) or (s2[i] in s2_to_s1):
            return False
        s1_to_s2.add(s1[i])
        s2_to_s1.add(s2[i])
    return True


def main():
    assert character_mapping("abc", "bcd")
    assert not character_mapping("foo", "bar")


if __name__ == '__main__':
    main()