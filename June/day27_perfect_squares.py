"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which
sum to n.
Example 1:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.
Example 2:
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.
"""

# My fullu dynamic programming solution. Gives a time limit exceeded error on Leetcode but works.
def numSquares(n: int) -> int:
    max_square = 1
    while (max_square + 1) ** 2 <= n:
        max_square += 1

    table = [[0 for j in range(n + 1)] for i in range(max_square + 1)]
    table[0] = [i for i in range(n + 1)]

    for row in range(1, max_square + 1):
        for col in range(1, n + 1):
            if col < row ** 2:
                table[row][col] = table[row - 1][col]
            else:
                table[row][col] = min(table[row - 1][col], table[row][col - row ** 2] + 1)

    for row in table:
        print(row)

    return table[-1][-1]


# A more effecient dp solution by another user on Leetcode that take less time than my own
def numSquares2(n):
    table = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        table[i] = min(table[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1

    return table[n]
# End second solution


# For testing

# print(numSquares(33))

#print(numSquares(7115))

print(numSquares(33))

"""
Leetcode test cases
4
6
7
10
12
13
15

1
2
3
5
8
9
11
14
16
19

18
21
22
23
24
25
26
27
28
29
30

31
32
33
34
36
37
39
40
41
43
44
"""