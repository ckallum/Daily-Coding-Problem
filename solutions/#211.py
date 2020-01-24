def pattern_indices(string, pattern):
    pat_len = len(pattern)
    result = []
    for i in range(len(string)-pat_len):
        if string[i:i+pat_len] == pattern:
            result.append(i)
    return result



def main():
    assert pattern_indices("abracadabra", "abr") == [0, 7]


if __name__ == '__main__':
    main()