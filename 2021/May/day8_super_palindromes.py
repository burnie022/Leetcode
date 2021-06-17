"""
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.
Given two positive integers left and right represented as strings, return the number of super-palindromes integers in
the inclusive range [left, right].

Example 1:
    Input: left = "4", right = "1000"
    Output: 4
    Explanation: 4, 9, 121, and 484 are superpalindromes.
        Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:
    Input: left = "1", right = "2"
    Output: 1

Constraints:
    --  1 <= left.length, right.length <= 18
    --  left and right consist of only digits.
    --  left and right cannot have leading zeros.
    --  left and right represent integers in the range [1, 1018].
    --  left is less than or equal to right.
"""


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # palindromes = []
        count = 0
        curr = left

        for i in [1, 4, 9, 121, 484]:
            print(f"{left} <= {i} <= {right} : {int(left) <= i <= int(right)}")
            if int(left) <= i <= int(right):
                count += 1

        if len(right) <= 4:
            return count

        if left < 10000:
            pass

        curr = left[:int(len(curr) / 2)]

        # prefix = 1
        # while (len(str(prefix)) * 2) + 2 <= len(right):
        #     print(curr, end="")
        #     # palindromes.append(curr)
        #     square = str(int(curr) ** 2)
        #     if square == square[::-1]:
        #         print(f" -- super palindrome square: {square}", end="")
        #         count += 1
        #
        #     mid = int(len(curr) / 2)
        #     center = curr[mid-1: mid+1] if len(curr) % 2 == 0 else curr[mid]
        #     if center[0] == '9':
        #         curr = '1' * (len(curr) + 1)
        #     else:
        #         curr = curr[mid+1:] + (str(int(center[0]) + 1) * len(center)) + curr[mid+1:]
        #     print("")
        #
        #     strlen = (len(str(prefix)) * 2) + len(str(center)) if int(prefix) else len(str(center))
        #
        # return count

        # while len(curr) <= len(right):
        #     print(curr, end="")
        #     # palindromes.append(curr)
        #     square = str(int(curr) ** 2)
        #     if square == square[::-1]:
        #         print(f" -- super palindrome square: {square}", end="")
        #         count += 1
        #
        #     mid = int(len(curr) / 2)
        #     center = curr[mid-1: mid+1] if len(curr) % 2 == 0 else curr[mid]
        #     if center[0] == '9':
        #         curr = '1' * (len(curr) + 1)
        #     else:
        #         curr = curr[mid+1:] + (str(int(center[0]) + 1) * len(center)) + curr[mid+1:]
        #     print("")


# Stupid solution to this Leetcode problem
class Stupid:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        super_palindromes = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121, 12102202520220121, 12104402820440121, 12122232623222121, 12124434743442121, 12321024642012321, 12323244744232321, 12343456865434321, 12345678987654321, 40000000800000004, 40004000900040004]
        l, r = int(left), int(right)
        count = 0

        for sp in super_palindromes:
            if l <= sp <= r:
                count += 1

        return count


# Test cases
obj = Stupid()
tests = [
    # ("1", "9999999999"),
    ("4", "1000")
]

for l, r in tests:
    print(f"\"{l}\"\n\"{r}\"")
    print(obj.superpalindromesInRange(l, r), end="\n\n")


# print("001") # "001"
# print(int("001")) # 1
# print(int("001") == True) # True
# print(int("000") == True) # False
# print("999" < "998") # False
