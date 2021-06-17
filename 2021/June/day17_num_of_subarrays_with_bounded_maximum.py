"""
We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that
subarray is at least left and at most right.

Example:
    Input:
        nums = [2, 1, 4, 3]
        left = 2
        right = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:
    - left, right, and nums[i] will be an integer in the range [0, 10^9].
    - The length of nums will be in the range of [1, 50000].
"""
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        increment = behind = next_behind = subarrays = 0

        for n in nums:
            if n > right:
                increment = behind = 0
            elif n < left:
                if increment:
                    subarrays += increment + behind
                next_behind += 1
            else:
                if next_behind:
                    behind += next_behind
                    next_behind = 0
                increment += 1
                subarrays += increment + behind

        return subarrays


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ([2, 1, 4, 3],2,3),
        ([3,2,1,4,5],2,5),
        ([2,1,4,5],2,5),
        ([1,2,3,2,1,4,5,5,4,3],2,5),
        ([1,2,3,2,1,6,4,5,5,4,3],2,5),
        ([1,2,3,2,1,1,4,5,5,4,3], 2, 5),
    ]

    for t in tests:
        print(t[0])
        print(t[1])
        print(t[2])
        print(obj.numSubarrayBoundedMax(*t), end="\n\n")


    # from random import randint
    #
    # def gen_test(length, max_n):
    #     return [randint(0, max_n) for _ in range(length)]
    # print(gen_test(10000,100))



"""
[2,1,4,3]
2
3
[3,2,1,4,5]
2
5
[2,1,4,5]
2
5
[1,2,3,2,1,4,5,5,4,3]
2
5
[1,2,3,2,1,6,4,5,5,4,3]
2
5
[12, 54, 94, 53, 70, 28, 61, 20, 10, 56, 60, 36, 50, 22, 74, 5, 6, 69, 51, 7, 90, 18, 14, 46, 100, 40, 56, 29, 51, 84, 73, 70, 93, 46, 83, 85, 55, 81, 19, 63, 62, 45, 95, 52, 99, 89, 7, 12, 28, 78, 55, 75, 73, 94, 37, 51, 13, 17, 65, 66, 46, 54, 53, 65, 95, 79, 1, 39, 42, 31, 100, 67, 76, 51, 48, 19, 37, 96, 25, 24, 38, 15, 77, 45, 3, 3, 0, 85, 53, 5, 19, 66, 32, 16, 83, 62, 50, 60, 19, 45, 18, 88, 53, 8, 59, 90, 17, 29, 2, 40, 54, 88, 29, 52, 1, 57, 51, 70, 11, 17, 79, 50, 22, 96, 10, 47, 52, 93, 91, 56, 3, 82, 52, 84, 57, 26, 32, 27, 90, 2, 91, 60, 35, 15, 5, 11, 81, 54, 14, 71, 12, 42, 84, 68, 16, 0, 84, 4, 39, 81, 36, 52, 87, 57, 6, 51, 79, 39, 39, 100, 99, 21, 54, 48, 17, 39, 43, 35, 47, 35, 71, 81, 26, 99, 66, 7, 13, 13, 79, 61, 27, 69, 1, 59, 25, 65, 52, 50, 19, 19, 36, 52, 56, 26, 85, 65, 47, 7, 19, 15, 84, 55, 75, 6, 40, 19, 51, 13, 78, 78, 64, 56, 27, 36, 74, 37, 40, 25, 8, 26, 64, 65, 80, 5, 16, 39, 2, 81, 44, 8, 5, 35, 4, 85, 28, 70, 45, 34, 63, 35, 71, 91, 3, 59, 57, 38, 43, 35, 13, 66, 17, 13, 68, 26, 42, 57, 49, 60, 11, 27, 51, 87, 6, 87, 56, 88, 100, 84, 36, 51, 35, 13, 93, 1, 10, 21, 11, 44, 100, 43, 61, 99, 40, 2, 8, 12, 12, 48, 21, 51, 59, 54, 85, 29, 53, 64, 24, 69, 26, 37, 17, 4, 67, 19, 88, 46, 78, 2, 68, 76, 90, 38, 68, 37, 75, 66, 63, 44, 18, 47, 84, 74, 93, 71, 62, 29, 72, 95, 87, 46, 55, 58, 8, 5, 22, 99, 3, 48, 12, 78, 87, 37, 27, 45, 20, 8, 92, 68, 62, 55, 68, 41, 41, 83, 95, 70, 87, 32, 87, 85, 9, 57, 18, 31, 66, 93, 22, 89, 51, 4, 86, 26, 71, 52, 91, 1, 66, 57, 84, 56, 67, 27, 82, 13, 85, 30, 51, 6, 100, 29, 5, 51, 80, 82, 39, 56, 65, 20, 97, 63, 59, 74, 79, 33, 88, 98, 35, 67, 88, 61, 70, 10, 34, 59, 65, 70, 21, 62, 32, 2, 64, 73, 68, 66, 75, 72, 85, 15, 87, 70, 59, 57, 52, 86, 67, 60, 37, 64, 69, 0, 76, 78, 96, 30, 99, 53, 97, 3, 12, 30, 77, 100, 2, 45, 79, 42, 35, 54, 88, 99, 55, 4, 15, 49, 39, 7, 30, 46, 58, 33, 89, 14, 96, 62, 29, 6, 100, 18, 38, 36, 60, 42, 49, 86, 59, 68, 44, 79, 36, 63]
25
75
[2,0,4,3]
2
3
[1,2,3,2,1,1,4,5,5,4,3]
2
5
[5,5,5]
2
5
[1,2,3,2,1,1,4,5]
2
5
[1,2,3,2,1,1,4]
2
5
[1,2,3,2,1,1]
2
5
[2,3,2,1,1]
2
5
[3,2,1,1]
2
5
[2,1,1]
2
5
[1,1,2]
2
5
[1,1]
2
5
[12, 54, 94, 53, 70, 28, 61, 20, 10, 56, 60, 36, 50, 22, 74, 5, 6, 69, 51, 7, 90, 18, 14, 46, 100, 40, 56, 29, 51, 84, 73, 70, 93, 46, 83, 85, 55, 81, 19, 63, 62, 45, 95, 52, 99, 89, 7, 12, 28, 78, 55, 75, 73, 94, 37, 51, 13, 17, 65, 66, 46, 54, 53, 65, 95, 79, 1, 39, 42, 31, 100, 67, 76, 51, 48, 19, 37, 96, 25, 24, 38, 15, 77, 45, 3, 3, 0, 85, 53, 5, 19, 66, 32, 16, 83, 62, 50, 60, 19, 45, 18, 88, 53, 8, 59, 90, 17, 29, 2, 40, 54, 88, 29, 52, 1, 57, 51, 70, 11, 17, 79, 50, 22, 96, 10, 47, 52, 93, 91, 56, 3, 82, 52, 84, 57, 26, 32, 27, 90, 2, 91, 60, 35, 15, 5, 11, 81, 54, 14, 71, 12, 42, 84, 68, 16, 0, 84, 4, 39, 81, 36, 52, 87, 57, 6, 51, 79, 39, 39, 100, 99, 21, 54, 48, 17, 39, 43, 35, 47, 35, 71, 81, 26, 99, 66, 7, 13, 13, 79, 61, 27, 69, 1, 59, 25, 65, 52, 50, 19, 19, 36, 52, 56, 26, 85, 65, 47, 7, 19, 15, 84, 55, 75, 6, 40, 19, 51, 13, 78, 78, 64, 56, 27, 36, 74, 37, 40, 25, 8, 26, 64, 65, 80, 5, 16, 39, 2, 81, 44, 8, 5, 35, 4, 85, 28, 70, 45, 34, 63, 35, 71, 91, 3, 59, 57, 38, 43, 35, 13, 66, 17, 13, 68, 26, 42, 57, 49, 60, 11, 27, 51, 87, 6, 87, 56, 88, 100, 84, 36, 51, 35, 13, 93, 1, 10, 21, 11, 44, 100, 43, 61, 99, 40, 2, 8, 12, 12, 48, 21, 51, 59, 54, 85, 29, 53, 64, 24, 69, 26, 37, 17, 4, 67, 19, 88, 46, 78, 2, 68, 76, 90, 38, 68, 37, 75, 66, 63, 44, 18, 47, 84, 74, 93, 71, 62, 29, 72, 95, 87, 46, 55, 58, 8, 5, 22, 99, 3, 48, 12, 78, 87, 37, 27, 45, 20, 8, 92, 68, 62, 55, 68, 41, 41, 83, 95, 70, 87, 32, 87, 85, 9, 57, 18, 31, 66, 93, 22, 89, 51, 4, 86, 26, 71, 52, 91, 1, 66, 57, 84, 56, 67, 27, 82, 13, 85, 30, 51, 6, 100, 29, 5, 51, 80, 82, 39, 56, 65, 20, 97, 63, 59, 74, 79, 33, 88, 98, 35, 67, 88, 61, 70, 10, 34, 59, 65, 70, 21, 62, 32, 2, 64, 73, 68, 66, 75, 72, 85, 15, 87, 70, 59, 57, 52, 86, 67, 60, 37, 64, 69, 0, 76, 78, 96, 30, 99, 53, 97, 3, 12, 30, 77, 100, 2, 45, 79, 42, 35, 54, 88, 99, 55, 4, 15, 49, 39, 7, 30, 46, 58, 33, 89, 14, 96, 62, 29, 6, 100, 18, 38, 36, 60, 42, 49, 86, 59, 68, 44, 79, 36, 63]
8
59
[12, 54, 94, 53, 70, 28, 61, 20, 10, 56, 60, 36, 50, 22, 74, 5, 6, 69, 51, 7, 90, 18, 14, 46, 100, 40, 56, 29, 51, 84, 73, 70, 93, 46, 83, 85, 55, 81, 19, 63, 62, 45, 95, 52, 99, 89, 7, 12, 28, 78, 55, 75, 73, 94, 37, 51, 13, 17, 65, 66, 46, 54, 53, 65, 95, 79, 1, 39, 42, 31, 100, 67, 76, 51, 48, 19, 37, 96, 25, 24, 38, 15, 77, 45, 3, 3, 0, 85, 53, 5, 19, 66, 32, 16, 83, 62, 50, 60, 19, 45, 18, 88, 53, 8, 59, 90, 17, 29, 2, 40, 54, 88, 29, 52, 1, 57, 51, 70, 11, 17, 79, 50, 22, 96, 10, 47, 52, 93, 91, 56, 3, 82, 52, 84, 57, 26, 32, 27, 90, 2, 91, 60, 35, 15, 5, 11, 81, 54, 14, 71, 12, 42, 84, 68, 16, 0, 84, 4, 39, 81, 36, 52, 87, 57, 6, 51, 79, 39, 39, 100, 99, 21, 54, 48, 17, 39, 43, 35, 47, 35, 71, 81, 26, 99, 66, 7, 13, 13, 79, 61, 27, 69, 1, 59, 25, 65, 52, 50, 19, 19, 36, 52, 56, 26, 85, 65, 47, 7, 19, 15, 84, 55, 75, 6, 40, 19, 51, 13, 78, 78, 64, 56, 27, 36, 74, 37, 40, 25, 8, 26, 64, 65, 80, 5, 16, 39, 2, 81, 44, 8, 5, 35, 4, 85, 28, 70, 45, 34, 63, 35, 71, 91, 3, 59, 57, 38, 43, 35, 13, 66, 17, 13, 68, 26, 42, 57, 49, 60, 11, 27, 51, 87, 6, 87, 56, 88, 100, 84, 36, 51, 35, 13, 93, 1, 10, 21, 11, 44, 100, 43, 61, 99, 40, 2, 8, 12, 12, 48, 21, 51, 59, 54, 85, 29, 53, 64, 24, 69, 26, 37, 17, 4, 67, 19, 88, 46, 78, 2, 68, 76, 90, 38, 68, 37, 75, 66, 63, 44, 18, 47, 84, 74, 93, 71, 62, 29, 72, 95, 87, 46, 55, 58, 8, 5, 22, 99, 3, 48, 12, 78, 87, 37, 27, 45, 20, 8, 92, 68, 62, 55, 68, 41, 41, 83, 95, 70, 87, 32, 87, 85, 9, 57, 18, 31, 66, 93, 22, 89, 51, 4, 86, 26, 71, 52, 91, 1, 66, 57, 84, 56, 67, 27, 82, 13, 85, 30, 51, 6, 100, 29, 5, 51, 80, 82, 39, 56, 65, 20, 97, 63, 59, 74, 79, 33, 88, 98, 35, 67, 88, 61, 70, 10, 34, 59, 65, 70, 21, 62, 32, 2, 64, 73, 68, 66, 75, 72, 85, 15, 87, 70, 59, 57, 52, 86, 67, 60, 37, 64, 69, 0, 76, 78, 96, 30, 99, 53, 97, 3, 12, 30, 77, 100, 2, 45, 79, 42, 35, 54, 88, 99, 55, 4, 15, 49, 39, 7, 30, 46, 58, 33, 89, 14, 96, 62, 29, 6, 100, 18, 38, 36, 60, 42, 49, 86, 59, 68, 44, 79, 36, 63]
3
27
[12, 54, 94, 53, 70, 28, 61, 20, 10, 56, 60, 36, 50, 22, 74, 5, 6, 69, 51, 7, 90, 18, 14, 46, 100, 40, 56, 29, 51, 84, 73, 70, 93, 46, 83, 85, 55, 81, 19, 63, 62, 45, 95, 52, 99, 89, 7, 12, 28, 78, 55, 75, 73, 94, 37, 51, 13, 17, 65, 66, 46, 54, 53, 65, 95, 79, 1, 39, 42, 31, 100, 67, 76, 51, 48, 19, 37, 96, 25, 24, 38, 15, 77, 45, 3, 3, 0, 85, 53, 5, 19, 66, 32, 16, 83, 62, 50, 60, 19, 45, 18, 88, 53, 8, 59, 90, 17, 29, 2, 40, 54, 88, 29, 52, 1, 57, 51, 70, 11, 17, 79, 50, 22, 96, 10, 47, 52, 93, 91, 56, 3, 82, 52, 84, 57, 26, 32, 27, 90, 2, 91, 60, 35, 15, 5, 11, 81, 54, 14, 71, 12, 42, 84, 68, 16, 0, 84, 4, 39, 81, 36, 52, 87, 57, 6, 51, 79, 39, 39, 100, 99, 21, 54, 48, 17, 39, 43, 35, 47, 35, 71, 81, 26, 99, 66, 7, 13, 13, 79, 61, 27, 69, 1, 59, 25, 65, 52, 50, 19, 19, 36, 52, 56, 26, 85, 65, 47, 7, 19, 15, 84, 55, 75, 6, 40, 19, 51, 13, 78, 78, 64, 56, 27, 36, 74, 37, 40, 25, 8, 26, 64, 65, 80, 5, 16, 39, 2, 81, 44, 8, 5, 35, 4, 85, 28, 70, 45, 34, 63, 35, 71, 91, 3, 59, 57, 38, 43, 35, 13, 66, 17, 13, 68, 26, 42, 57, 49, 60, 11, 27, 51, 87, 6, 87, 56, 88, 100, 84, 36, 51, 35, 13, 93, 1, 10, 21, 11, 44, 100, 43, 61, 99, 40, 2, 8, 12, 12, 48, 21, 51, 59, 54, 85, 29, 53, 64, 24, 69, 26, 37, 17, 4, 67, 19, 88, 46, 78, 2, 68, 76, 90, 38, 68, 37, 75, 66, 63, 44, 18, 47, 84, 74, 93, 71, 62, 29, 72, 95, 87, 46, 55, 58, 8, 5, 22, 99, 3, 48, 12, 78, 87, 37, 27, 45, 20, 8, 92, 68, 62, 55, 68, 41, 41, 83, 95, 70, 87, 32, 87, 85, 9, 57, 18, 31, 66, 93, 22, 89, 51, 4, 86, 26, 71, 52, 91, 1, 66, 57, 84, 56, 67, 27, 82, 13, 85, 30, 51, 6, 100, 29, 5, 51, 80, 82, 39, 56, 65, 20, 97, 63, 59, 74, 79, 33, 88, 98, 35, 67, 88, 61, 70, 10, 34, 59, 65, 70, 21, 62, 32, 2, 64, 73, 68, 66, 75, 72, 85, 15, 87, 70, 59, 57, 52, 86, 67, 60, 37, 64, 69, 0, 76, 78, 96, 30, 99, 53, 97, 3, 12, 30, 77, 100, 2, 45, 79, 42, 35, 54, 88, 99, 55, 4, 15, 49, 39, 7, 30, 46, 58, 33, 89, 14, 96, 62, 29, 6, 100, 18, 38, 36, 60, 42, 49, 86, 59, 68, 44, 79, 36, 63]
1
89
[12, 54, 94, 53, 70, 28, 61, 20, 10, 56, 60, 36, 50, 22, 74, 5, 6, 69, 51, 7, 90, 18, 14, 46, 100, 40, 56, 29, 51, 84, 73, 70, 93, 46, 83, 85, 55, 81, 19, 63, 62, 45, 95, 52, 99, 89, 7, 12, 28, 78, 55, 75, 73, 94, 37, 51, 13, 17, 65, 66, 46, 54, 53, 65, 95, 79, 1, 39, 42, 31, 100, 67, 76, 51, 48, 19, 37, 96, 25, 24, 38, 15, 77, 45, 3, 3, 0, 85, 53, 5, 19, 66, 32, 16, 83, 62, 50, 60, 19, 45, 18, 88, 53, 8, 59, 90, 17, 29, 2, 40, 54, 88, 29, 52, 1, 57, 51, 70, 11, 17, 79, 50, 22, 96, 10, 47, 52, 93, 91, 56, 3, 82, 52, 84, 57, 26, 32, 27, 90, 2, 91, 60, 35, 15, 5, 11, 81, 54, 14, 71, 12, 42, 84, 68, 16, 0, 84, 4, 39, 81, 36, 52, 87, 57, 6, 51, 79, 39, 39, 100, 99, 21, 54, 48, 17, 39, 43, 35, 47, 35, 71, 81, 26, 99, 66, 7, 13, 13, 79, 61, 27, 69, 1, 59, 25, 65, 52, 50, 19, 19, 36, 52, 56, 26, 85, 65, 47, 7, 19, 15, 84, 55, 75, 6, 40, 19, 51, 13, 78, 78, 64, 56, 27, 36, 74, 37, 40, 25, 8, 26, 64, 65, 80, 5, 16, 39, 2, 81, 44, 8, 5, 35, 4, 85, 28, 70, 45, 34, 63, 35, 71, 91, 3, 59, 57, 38, 43, 35, 13, 66, 17, 13, 68, 26, 42, 57, 49, 60, 11, 27, 51, 87, 6, 87, 56, 88, 100, 84, 36, 51, 35, 13, 93, 1, 10, 21, 11, 44, 100, 43, 61, 99, 40, 2, 8, 12, 12, 48, 21, 51, 59, 54, 85, 29, 53, 64, 24, 69, 26, 37, 17, 4, 67, 19, 88, 46, 78, 2, 68, 76, 90, 38, 68, 37, 75, 66, 63, 44, 18, 47, 84, 74, 93, 71, 62, 29, 72, 95, 87, 46, 55, 58, 8, 5, 22, 99, 3, 48, 12, 78, 87, 37, 27, 45, 20, 8, 92, 68, 62, 55, 68, 41, 41, 83, 95, 70, 87, 32, 87, 85, 9, 57, 18, 31, 66, 93, 22, 89, 51, 4, 86, 26, 71, 52, 91, 1, 66, 57, 84, 56, 67, 27, 82, 13, 85, 30, 51, 6, 100, 29, 5, 51, 80, 82, 39, 56, 65, 20, 97, 63, 59, 74, 79, 33, 88, 98, 35, 67, 88, 61, 70, 10, 34, 59, 65, 70, 21, 62, 32, 2, 64, 73, 68, 66, 75, 72, 85, 15, 87, 70, 59, 57, 52, 86, 67, 60, 37, 64, 69, 0, 76, 78, 96, 30, 99, 53, 97, 3, 12, 30, 77, 100, 2, 45, 79, 42, 35, 54, 88, 99, 55, 4, 15, 49, 39, 7, 30, 46, 58, 33, 89, 14, 96, 62, 29, 6, 100, 18, 38, 36, 60, 42, 49, 86, 59, 68, 44, 79, 36, 63]
0
20

"""
