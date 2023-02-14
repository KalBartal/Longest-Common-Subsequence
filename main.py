def lcs(text1, text2):
    m = len(text1)
    n = len(text2)

    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # lcs[I][j] will store the length of
    # longest common subsequence of text1[0..i-1]
    # and text2[0..j-1]
    lcs = [[None]*(n + 1) for i in range(m + 1)]

    # fill table in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    # lcs[m][n] contains the length of
    # the longest common subsequence of
    # text1[0..n-1] and text2[0..m-1]
    return lcs[m][n]


# Driver code
text1 = "ABCDE"
text2 = "ABLE"
print(lcs(text1, text2))

# Output: 3
