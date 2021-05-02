"""
THIS IS A DIFFICULT PROBLEM

Given an array of digits, you can write numbers using each digits[i] as many times as we want.
For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a
given integer n.

Example 1:
    Input: digits = ["1","3","5","7"], n = 100
    Output: 20
    Explanation:
        The 20 numbers that can be written are:
        1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:
    Input: digits = ["1","4","9"], n = 1000000000
    Output: 29523
    Explanation:
        We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
        81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
        2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
        In total, this is 29523 integers that can be written using the digits array.
Example 3:
    Input: digits = ["7"], n = 8
    Output: 1

Constraints:
    1 <= digits.length <= 9
    digits[i].length == 1
    digits[i] is a digit from '1' to '9'.
    All the values in digits are unique.
    1 <= n <= 109
"""

def atMostNGivenDigitSet(digits, n: int) -> int:
    n = str(n)
    less_digit_sum = sum(len(digits) ** e for e in range(1, len(n)))

    same_digit_sum = 0
    for i in range(len(n)):
        num_digits_smaller = len([d for d in digits if d < n[i]])
        same_digit_sum += (num_digits_smaller * (len(digits) ** (len(n) - 1 - i)))
        if n[i] not in digits:
            break

    return less_digit_sum + same_digit_sum + all([n_digit in digits for n_digit in n])


# Test cases
tests = [
    (["1","3","5","7"], 100),
    (["1","3","5","7"], 50),
    (["1","4","9"], 1000000000),
    (["1","4","9"], 921802300),
    (["7"], 8),
    (["7"], 7),
    (["2","3","5"], 352),
    (["7"], 6),
    (["1","3","5","7"], 5367)
]

for t in tests:
    print(f"{t[0]}, n = {t[1]} : ", end="")
    print(atMostNGivenDigitSet(*t), end="\n")

