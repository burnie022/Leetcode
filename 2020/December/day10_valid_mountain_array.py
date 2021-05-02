"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
            arr[0] < arr[1] < ... < arr[i - 1] < A[i]
            arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

[ 0, 2, 3, 4, 5, 2, 1, 0 ]
    Valid mountain array, strictly increasing, then decreasing

[ 0, 2, 3, 3, 5, 2, 1, 0 ]
    Not valid, increasing but not strictly, then decreasing

Example 1:
    Input: arr = [2,1]
    Output: false
Example 2:
    Input: arr = [3,5,5]
    Output: false
Example 3:
    Input: arr = [0,3,2,1]
    Output: true

Constraints:
    1 <= arr.length <= 104
    0 <= arr[i] <= 104

Hint
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just
need to be able to determine the start of the valley in the mountain and from that point onwards, it should
be a valley i.e. no mini-hills after that. Use this information in regards to the values in the array and
you will be able to come up with a straightforward solution.
"""

def validMountainArray(arr) -> bool:
    if len(arr) < 3:
        return False
    if arr[0] >= arr[1]:
        return False
    decreasing = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1] and not decreasing:
            continue
        elif arr[i] < arr[i - 1]:
            if not decreasing:
                decreasing = True
        else:
            return False
    return decreasing


# Test cases
tests = [
[2,1],
[3,5,5],
[0,3,2,1],
[ 0, 2, 3, 4, 5, 2, 1, 0 ],
[ 0, 2, 3, 3, 5, 2, 1, 0 ]

]

for t in tests:
    print(t)
    print(validMountainArray(t))


