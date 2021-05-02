"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal
order as shown in the below image.

Example:
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output:  [1,2,4,7,5,3,6,8,9]

    Explanation: VIEW EXAMPLE PIC

Note:
    The total number of elements of the given matrix will not exceed 10,000.
"""
from typing import List

def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    result = []
    reverse = True
    for i in range(len(matrix[0]) + len(matrix) - 1):
        curr = []
        col = i
        start = 0
        if col >= len(matrix[0]):
            start = col - len(matrix[0])
            col = len(matrix[0])
        for row in range(start, len(matrix)):
            if col < len(matrix[0]) and row < len(matrix):
                curr.append(matrix[row][col])
            col -= 1
            if col < 0:
                break

        if reverse:
            curr = curr[::-1]
        result.extend(curr)
        reverse = not reverse

    return result



# Test cases

tests = [
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ],
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ],
    [
        [1],
        [2],
        [3]
    ],
    [
        [1, 2, 3, 4]
    ],
    [
        [1]
    ]
]


for t in tests:
    print(t)
    # print(findDiagonalOrder(t), end="\n\n")

t1 = []
li = []
for i in range(1, 10001):
    li.append(i)
    if len(li) == 100:
        t1.append(li)
        li = []

print(t1)
# print(findDiagonalOrder(t1))
