"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of
1's in their binary representation and return them as an array.
Example 1:
    Input: 2
    Output: [0,1,1]
Example 2:
    Input: 5
    Output: [0,1,1,2,1,2]
Follow up:
    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear
    time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in
    any other language.
Hint #1
You should make use of what you have produced already.
Hint #2
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Hint #3
Or does the odd/even status of the number help you in calculating the number of 1s?
"""

def countBits(num: int):
    binary_ones = [0, 1]
    bit, next_bit = 2, 4
    half_bit, increment_range = bit // 2, 2 + 1

    if num == 0 or num == 1:
        return binary_ones[:1 + num]

    for i in range(2, 1 + num):
        if i < increment_range:
            binary_ones.append(binary_ones[-half_bit])
        else:
            binary_ones.append(1 + binary_ones[-half_bit])

        if i + 1 == next_bit:
            bit = next_bit
            next_bit *= 2
            half_bit = bit // 2
            increment_range = bit + half_bit

    return binary_ones


# For testing

n = 64

print(countBits(n))
"""
li = [0,1]
bit, next_bit = 2, 4
half, increment_range = bit//2, 2 + 1
for i in range(0, 513):
    if i < 2:
        print(i, ":", li[i])
        continue
    else:
        if i < increment_range:
            li.append(li[-half])
        else:
            li.append(1 + li[-half])

        if i + 1 == next_bit:
            bit = next_bit
            next_bit *= 2
            half = bit // 2
            increment_range = bit + half

    print(i, ":", li[-1], end="")

    n = bin(i)
    c = n.count("1")
    # #t += c
    # #if i % 2 == 0:
    # print(i, ":", c)
    print(",", c, end=", ")
    print(li[-1] == c)
"""
