"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:
    Input: word1 = "leetcode", word2 = "etco"
    Output: 4

Constraints:
    1 <= word1.length, word2.length <= 500
    word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i > 0 and j > 0 else 1

                    for k in range(j+1, len(word1)):
                        if i > 0:
                            dp[i][k] = max(dp[i-1][k-1], dp[i][j])
                        else:
                            dp[i][k] = dp[i][j]
                    break

        for row in dp:
            print(row)

        match_length = max(row[-1] for row in dp)
        print(match_length)
        return (len(word1) - match_length) + (len(word2) - match_length)



# A leetcoder's solution
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return len(word1) + len(word2) - 2 * dp[-1][-1]



# Test cases
obj = Solution2()
tests = [
    ("sea", "eat"),
    ("leetcode", "etco"),
    ("joserivas", "serrivas")
]

for t in tests:
    print(obj.minDistance(*t))
