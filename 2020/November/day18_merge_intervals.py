"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the
intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""

def merge(intervals):
    if len(intervals) < 2:
        return intervals

    new_intervals = []
    stack = []
    for s, e in intervals:
        stack.append((s, False))
        stack.append((e, True))
    print(sorted(stack))

    start_val, count = None, 0
    for num, end in sorted(stack):
        if start_val is None:
            start_val = num

        count += -1 if end else 1

        if count == 0:
            new_intervals.append([start_val, num])
            start_val = None

    return new_intervals


# Test cases
tests = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[2,4],[1,2],[15,18],[10,16]],
    [[2,2],[2,2],[2,2]],
    [[2,2],[2,2],[2,2],[2,3]],
    [[1,4],[0,4]]
]

for t in tests:
    print(t)
    print(merge(t), end="\n\n")
