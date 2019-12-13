def gray_codes(n):
    results = list()
    results.append("0")
    results.append("1")
    for i in range(n-1):
        for num in results[::-1]:
            results.append(num)
        l = len(results)//2
        for j in range(l):
            results[j] = '0' + results[j]
            results[j+l] = '1'+results[j+l]
    print(results)
    return results

def main():
    assert gray_codes(2) == ['00', '01', '11', '10']


if __name__ == '__main__':
    main()

