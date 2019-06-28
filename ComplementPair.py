def findComplement(nums, k):
    compList = {}
    for x in nums:
        if k-x in compList:
            return True
        else:
            compList[x] = x
    return False

def main():
    l = [1,1,2,3,4,5,5,0,7,8,9]
    k = int(input('Enter a number: '))
    print('The result is', findComplement(l, k))

if __name__ == "__main__":
    main()
