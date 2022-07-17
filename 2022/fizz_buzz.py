"""
Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]
Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]
Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
    1 <= n <= 10^4
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            if not (i + 1) % 3 and not (i + 1) % 5:
                res.append("FizzBuzz")
            elif not (i + 1) % 3:
                res.append("Fizz")
            elif not (i + 1) % 5:
                res.append("Buzz")
            else:
                res.append(f"{i + 1}")

        return res


if __name__ == "__main__":
    obj = Solution()
    tests = [
        3, 5, 15
    ]

    for t in tests:
        print(t)
        print(obj.fizzBuzz(t), end="\n\n")
