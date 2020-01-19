def permutation(letters, perm):
    result = [0]*len(letters)
    for index, p in enumerate(perm):
        result[p] = letters[index]
    return result



def main():
    assert permutation(["a", "b", "c"], [2, 1, 0]) == ["c", "b", "a"]


if __name__ == '__main__':
    main()
