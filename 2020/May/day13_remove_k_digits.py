"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
def removeKdigits(num: str, k: int) -> str:
    if k >= len(num) - num.count("0"):
        return "0"
    if not k:
        return num
    num = list(num)
    for i in range(1, len(num)):
        if not k:
            break
        if int(num[i]) < int(num[i - 1]):
            for j in range(i - 1, -1, -1):
                if num[j] == "":
                    continue
                if int(num[j]) > int(num[i]) and k > 0:
                    num[j] = ""
                    k -= 1
                else:
                    break

    while k > 0:
        num.pop()
        k -= 1

    start = 0
    while num[start] == "0" or num[start] == "":
        start += 1
        if start == len(num):
            return "0"

    return "".join(num[start:])

# For testing
# nums = list("172345634567")
# idx = 7
# kay = 2
# for j in range(idx - 1, 0, -1):
#     if int(nums[j]) > int(nums[idx]) and kay:
#         nums[j] = ""
#         kay -= 1
#     else:
#         break
# print("My test:", nums)

tests = {"1200": 2,
         "123456": 1,
         "12345": 3,
         "1432219": 3,
         "10200": 1,
         "10" : 2,
         "100": 1,
         "1234000": 2,
         "123423456": 2,
         "4325043": 3,
         "765028321": 5,
         "121198": 2,
         "172345634567": 2}

for key, value in tests.items():
    print(key,":", value)
    print(removeKdigits(key, value))
