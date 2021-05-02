"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and
empty spaces . The integer division should truncate toward zero.

Example 1:
    Input: "3+2*2"
    Output: 7
Example 2:
    Input: " 3/2 "
    Output: 1
Example 3:
    Input: " 3+5 / 2 "
    Output: 5
Note:
    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
"""

def calculate(s: str) -> int:
    operators = ["/", "*", "-", "+"]

    def perform_operation(val1, val2, op):
        if op == "/":
            return int(val1 / val2)
        elif op == "*":
            return val1 * val2
        elif op == "+":
            return val1 + val2
        elif op == "-":
            return val1 - val2

    nums = []
    num = 0
    for ch in s:
        if ch == " ":
            continue
        if ch not in operators:
            num = (num * 10) + int(ch)
        else:
            nums.append(num)
            nums.append(ch)
            num = 0
    nums.append(num)

    for op1, op2 in [("/", "*"), ("-", "+")]:
        for i in range(1, len(nums) - 1):
            if nums[i] == op1 or nums[i] == op2:
                nums[i + 1] = perform_operation(nums[i - 1], nums[i + 1], nums[i])
                nums[i] = nums[i - 1] = " "

        while " " in nums:
            nums.remove(" ")

    return nums[0]

# Test cases

tests = [
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
    "3*2*2",
    "32* 2",
    "10",
    "10+20/5-3*2*6/1*2",
    "1-1+1",
    "2/2*2",
    "1+2*5/3+6/4*2"
]

for t in tests:
    print(t)
    print(calculate(t), end="\n\n")
