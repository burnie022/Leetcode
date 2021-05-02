"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique
permutations in any order.

Example 1:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
     [1,2,1],
     [2,1,1]]
Example 2:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
"""
from itertools import permutations

def permuteUniqueOneLiner(nums):
    return list(set(permutations(nums)))


from math import factorial

def permuteUnique(nums):
    if len(nums) == 1:
        return nums

    total_lists = factorial(len(nums))
    perms_list = [nums for i in range(total_lists)]
    print(perms_list)
    print(len(perms_list))

    def generate_repeating_nums(li, times_to_repeat_num):
        idx, times_repeated = 0, 0
        print(f"list generator received: {li}, time to repeat: {times_to_repeat_num}")
        while li:
            if times_repeated >= times_to_repeat_num:
                idx += 1
                times_repeated = 0
                if idx == len(li):
                    idx = 0
            # print(li[idx])
            yield li[idx]
            times_repeated += 1


    for index in range(len(nums)):
        curr_len = len(nums[index:])
        curr_factorial = int(factorial(curr_len) / curr_len)
        num_gen = generate_repeating_nums(nums[index:], curr_factorial)
        curr = 0
        for current_list in perms_list:
            if curr == curr_factorial:
                num_gen = generate_repeating_nums(nums[index:], curr_factorial)
                curr = 0
            nex = next(num_gen)
            print(f"next num to be added: {nex}")
            current_list[index] = nex
            curr += 1


    # current_list, index = 0, 0
    # while index < len(nums) - 1:
    #     switch_index = index
    #     curr_len = len(nums[index:])
    #     curr_factorial = int(factorial(curr_len) / curr_len)
    #     while switch_index < len(nums):
    #
    #
    #         for _ in range(curr_factorial):
    #             if index != switch_index:
    #                 perms_list[current_list][index], perms_list[current_list][switch_index] = \
    #                     perms_list[current_list][switch_index], perms_list[current_list][index]
    #                 if index == 1 and current_list == 2:
    #                     perms_list[index][1] = 5
    #             current_list += 1
    #
    #         switch_index += 1
    #
    #         if current_list == total_lists:
    #             index += 1
    #             current_list = 0
    #             break


    return perms_list

# Test cases

tests = [
    [1,1,2],
    [1,2,3],
    [1,2,3,4]
]

# for t in tests:
#     print(t)
#     print(permuteUniqueOneLiner(t))
#
# print(len(permuteUniqueOneLiner(tests[1])))

# print(permuteUnique(tests[1]))


# def generate_repeating_nums(li=[1,2,3], times_to_repeat_num=2):
#     idx, times_repeated = 0, 0
#     print(li)
#     while li:
#         if times_repeated >= times_to_repeat_num:
#             idx += 1
#             times_repeated = 0
#             if idx == len(li):
#                 idx = 0
#         # print(li[idx])
#         yield li[idx]
#         times_repeated += 1
#
# gen = generate_repeating_nums([2,3], 1)
#
# for _ in range(20):
#     print(next(gen))

def permutation_generator(li):
    places = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
    length = len(li)
    operation = 1
    yield li

    while True:
        if operation == places[length]:
            operation = 1
        for place in range(length, 0, -1):
            if operation % places[place] == 0:
                # li[-1], li[-1-place] = li[-1-place], li[-1]
                li[0], li[place] = li[place], li[0]
                operation += 1

                yield li
                break

my_gen = permutation_generator(tests[2])
ans = []
for _ in range(24):
    li = tuple(next(my_gen))
    ans.append(li)
    print(ans[-1])

print(len(ans))

s= set()
for li in ans:
    # print(li)
    s.add(tuple(li))

print(len(s))
print(ans)




