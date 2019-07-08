def prefixFunc(l, pre):
    return list(filter(lambda x: x[:len(pre)] == pre, l))

def main():
    l = ['dog', 'deer', 'deal', 'd']
    print(prefixFunc(l, 'de'))


if __name__ == '__main__':
    main()
