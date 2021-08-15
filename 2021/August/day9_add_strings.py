"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You
must also not convert the inputs to integers directly.

Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134"
Example 2:
    Input: num1 = "456", num2 = "77"
    Output: "533"
Example 3:
    Input: num1 = "0", num2 = "0"
    Output: "0"

Constraints:
    1 <= num1.length, num2.length <= 10^4
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        num1, num2 = num1[::-1], num2[::-1]
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        carry = 0
        for i, n in enumerate(num1):
            asc = ord(n) - 48
            if carry:
                carry -= 1
                asc += 1

            if i < len(num2):
                asc += ord(num2[i]) - 48

            if asc > 9:
                asc -= 10
                carry += 1

            ans.append(str(asc))

        if carry:
            ans.append("1")

        return "".join(ans[::-1])


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ("11", "123"),
        ("456", "77"),
        ("0", "0"),
        ("999", "999"),
        ("1", "9"),
        ("999876454345456756768156416416646464647647474664584646146497582346475879612031201246094379784102412410",
         "9999987546130212457815012041465237965729459756310341301646102215024120805785490569401236141061024120465102"),
    ]

    for t in tests:
        print(f"\"{t[0]}\"")
        print(f"\"{t[1]}\"")
        # print(obj.addStrings(*t), end="\n\n")
