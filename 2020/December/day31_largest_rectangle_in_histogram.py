"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
    Input: [2,1,5,6,2,3]
    Output: 10
"""
from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    if not heights:
        return 0
    stack, start = [], []
    max_area = heights[0]

    for i, n in enumerate(heights):
        if not stack or n > stack[-1]:
            stack.append(n)
            start.append(i)
            continue
        if n < stack[-1]:
            s = None
            while stack and stack[-1] > n:
                s = start.pop()
                max_area = max(max_area, stack.pop() * (i - s))
            start.append(s)
            stack.append(n)

    while stack:
        i = start.pop()
        n = stack.pop()
        max_area = max(max_area, n * (len(heights) - i))

    return max_area


# Test cases
tests = [
    [2,1,5,6,2,3],
    [1,2,2,1,1],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,31,5,6,7,8,9,10],
    [2,1,1,2,2,3],
    [6,3,5,4,5,1,6],
    [6,2,5,4,5,1,6],
    [1,3,2,1,2],
    [1,3,5,3,2,2,3,3,1,0,3,6],
    [1,3,5,3,0,2,6,6,1,0,3,6],
    [0],
    [],
    [1]
]

for t in tests:
    print(t)
    print(largestRectangleArea(t), end="\n\n")
