"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number
of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
Example 1:
    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
Example 2:
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
    Input: amount = 10, coins = [10]
    Output: 1
Note: You can assume that:
    0 <= amount <= 5000
    1 <= coin <= 5000
    the number of coins is less than 500
    the answer is guaranteed to fit into signed 32-bit integer
"""

"""
MY EXAMPLEs FOR HOW THIS CODE WORKS:
Create a table like this, where:
 
amount = 5 and coins = [1,2,5]
        0  1  2  3  4  5   <-- amount
       _________________
    1 | 1  1  1  1  1  1
    2 | 1  1  2  2  3  3
    5 | 1  1  2  2  3  4
    ^
    coins
Answer = 4
    
    
amount = 10, coins = [2, 3, 5, 10]
        0  1  2  3  4  5  6  7  8  9  10   <-- amount
       _________________________________
    2 | 1  0  1  0  1  0  1  0  1  0  1
    3 | 1  0  1  1  1  1  2  1  2  2  2
    5 | 1  0  1  1  1  2  2  2  3  3  4
    10| 1  0  1  1  1  2  2  2  3  3  5
    ^
    coins
Answer = 5

"""

def change(amount: int, coins) -> int:
    if amount == 0:
        return 1
    if not coins:
        return 0
    rows, cols = len(coins), amount + 1
    dp = [[0 for col in range(cols)] for row in range(rows)]

    for col in range(cols):
        dp[0][col] = 1 if col % coins[0] == 0 else 0

    for row in range(1, rows):
        for col in range(cols):
            dp[row][col] = dp[row-1][col] if col < coins[row] else dp[row][col - coins[row]] + dp[row-1][col]

    return dp[-1][-1]


# For testing
tests = [(5, [1,2,5]),
         (3, [2]),
         (10, [10]),
         (0, [10]),
         (10, []),
         (0, [])]
for a, b in tests:
    print("amount =", a, ", coins =", b, ", answer:", change(a,b))
# print(change(5, [1,2,5]))
