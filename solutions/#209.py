def lcs3(string1, string2, string3):
    dp = [[[0 for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]for _ in range(len(string3)+1)]
    for i in range(len(string3)+1):
        for j in range(len(string2)+1):
            for k in range(len(string1)+1):
                if i == 0 or j == 0 or k == 0:
                    continue
                elif string1[k-1] == string2[j-1] == string3[i-1]:
                    dp[i][j][k] = 1+dp[i-1][j-1][k-1]
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[len(string3)][len(string2)][len(string1)]


def main():
    assert lcs3("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious") == 5


if __name__ == '__main__':
    main()