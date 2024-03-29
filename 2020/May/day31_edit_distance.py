"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character
Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
"""

def minDistance(word1: str, word2: str) -> int:
    # This function uses the Levenshtein distance algorith with a full matrix to take a dynamic approach
    # of solving the problem
    lev = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]

    for i in range(1, len(word1) + 1):
        lev[0][i] = 1 + lev[0][i - 1]

    for j in range(1, len(word2) + 1):
        for i in range(len(word1) + 1):
            if i == 0:
                lev[j][i] = 1 + lev[j - 1][i]
            else:
                replacement_cost = 0 if word1[i-1] == word2[j-1] else 1
                lev[j][i] = min(1 + lev[j][i-1], 1 + lev[j-1][i],
                                replacement_cost + lev[j-1][i-1])

    for row in lev:
        print(row)
    return lev[-1][-1]


# For testing
tests = {("horse", "ros"),
         ("saturday", "sunday"),
         ("intention", "execution"),
         ("kitten", "sitting")}
for w1, w2 in tests:
    print("Min Dist for", w1, w2, ":", minDistance(w1, w2))
