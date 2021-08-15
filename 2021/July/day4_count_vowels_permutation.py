"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
    - Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    - Each vowel 'a' may only be followed by an 'e'.
    - Each vowel 'e' may only be followed by an 'a' or an 'i'.
    - Each vowel 'i' may not be followed by another 'i'.
    - Each vowel 'o' may only be followed by an 'i' or a 'u'.
    - Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:
    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:
    Input: n = 5
    Output: 68

Constraints:
    1 <= n <= 2 * 10^4

Hint #1
    Use dynamic programming.
Hint #2
    Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
Hint #3
    Deduce the recurrence from the given relations between vowels.
"""


# Optimal Solution using dynamic programming, and map implmented as 0-indexed list for faster processing than dict.
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        map = [[1], [0,2], [0,1,3,4],[2,4],[0]]
        memo = [1, 1, 1, 1, 1]

        for i in range(1, n):
            next_memo = [0, 0, 0, 0, 0]
            for j in range(5):
                for val in map[j]:
                    next_memo[val] += memo[j]
            memo = next_memo

        return sum(memo) % ((10 ** 9) + 7)


# Slow solution using recursion (DFS) and memoization, high memory use. Also works fine.
    def countVowelPermutationDFS(self, n: int) -> int:
        map = {
            1: [2], 2: [1, 3], 3: [1, 2, 4, 5], 4: [3, 5], 5: [1]
        }
        memo = [[0, 0, 0, 0, 0] for _ in range(n+1)]
        self.count = 0

        def dfs(val, count):
            if count == n:
                self.count += 1
                return 1
            if memo[count][val-1]:
                self.count += memo[count][val-1]
                return memo[count][val-1]

            total = 0
            for v in map[val]:
                total += dfs(v, count+1)
            memo[count][val-1] = total
            return total

        for key in map.keys():
            dfs(key, 1)

        return self.count % ((10 ** 9) + 7)


if __name__ == "__main__":
    obj = Solution()
    tests = [
        1, 2, 3, 5, 8, 10
    ]

    for t in tests:
        print(t)
        print(obj.countVowelPermutation(t), end="\n\n")

