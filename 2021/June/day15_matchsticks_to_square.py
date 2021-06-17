"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use
all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick
must be used exactly one time.
Return true if you can make this square and false otherwise.

Example 1:
    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
    Input: matchsticks = [3,3,3,3,4]
    Output: false
    Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:
    1 <= matchsticks.length <= 15
    0 <= matchsticks[i] <= 10^9
Hint #1
    Treat the matchsticks as an array. Can we split the array into 4 equal halves?
Hint #2
    Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
Hint #3
    For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. We can make use
    of recursion for this.
Hint #4
    We don't really need to keep track of which matchsticks belong to a particular side during recursion. We just need
     to keep track of the length of each of the 4 sides.
Hint #5
    When all matchsticks have been used we simply need to see the length of all 4 sides. If they're equal, we have a
    square on our hands!
"""
from typing import List



class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if len(matchsticks) < 4 or s % 4 != 0 or matchsticks[0] > s // 4:
            return False
        matchsticks = sorted(matchsticks, reverse=True)
        used = [0 for _ in range(len(matchsticks))]
        side = s // 4

        for i in range(4):
            curr = 0
            for j in range(len(matchsticks)):
                if not used[j] and curr + matchsticks[j] <= side:
                    curr += matchsticks[j]
                    used[j] = 1

            if curr != side:
                return False

        return Truef


# a leetcoder's solution
def makesquare(self, matchsticks: List[int]) -> bool:
    s = sum(matchsticks)
    if not matchsticks or s % 4:
        return False
    used = [0] * len(matchsticks)
    side = s // 4

    def dfs(wall, curr, m, seen, start):
        if wall == 1:
            return True
        if curr == side:
            return dfs(wall - 1, 0, m, seen, 0)
        for i in range(start, len(m)):
            if not seen[i] and curr + m[i] <= side:
                seen[i] = 1
                if dfs(wall, curr + m[i], m, seen, i + 1):
                    return True
                seen[i] = 0
        return False

    return dfs(4, 0, matchsticks, used, 0)






if __name__ == "__main__":
    obj = Solution()
    tests = [
        [1, 1, 2, 2, 2],
        [3, 3, 3, 3, 4],
        [5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3], # should be true 160/173
    ]

    for t in tests:
        print(t)
        # print(obj.makesquare(t), end="\n\n")
