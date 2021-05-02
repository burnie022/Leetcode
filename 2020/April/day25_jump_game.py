nums = [3,3,1,2,3,0,2,1,1]
# [2,3,1,1,4]
# [3,3,1,2,3,2,2,1,1]


def canJump(nums):
    if 0 not in nums:
        return True

    def jump(nums):
        #print("Current list: " + str(nums))
        if nums[0] >= len(nums) - 1:
            return True
        if nums[0] == 0:
            return False
        if nums[0] == 1:
            return jump(nums[1:])

        jump_range = []
        decrement = nums[0] - 1
        for i in range(1, nums[0] + 1):
            jump_range.append(nums[i] - decrement)
            decrement -= 1

        max_jump = max(jump_range)
        jump_index = len(jump_range) - list(reversed(jump_range)).index(max_jump) - 1
        next_index = jump_index + 1

        return jump(nums[next_index:])

    return jump(nums)

print(canJump(nums))
"""
# For my testing purposes
jump_range =[]
curr_index = 0
# check jump range
decrement = nums[curr_index] - 1
for i in range(curr_index + 1, curr_index + 1 + nums[curr_index]):
    jump_range.append(nums[i] - decrement)
    decrement -= 1
print(jump_range)
# check index
max_jump = max(jump_range)
print(max_jump)
jump_index = len(jump_range) - list(reversed(jump_range)).index(max_jump) - 1
next_index = curr_index + jump_index + 1
print(jump_index)
print("Next jump index: " + str(next_index))
print("Sliced list: " + str(nums[next_index:]))"""