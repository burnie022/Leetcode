nums = [3,3]
target = 6


def twoSum(nums, target):
    n_dict = {}
    for n in range(len(nums)):
        diff = target - nums[n]
        if n_dict.get(diff) is not None:
            return [n, n_dict[diff]]
        n_dict[nums[n]] = n


print(twoSum(nums, target))
