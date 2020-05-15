def singleNonDuplicate(nums) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if lo == hi:
            return nums[lo]

        if nums[mid - 1] == nums[mid]:
            if len(nums[:mid + 1]) % 2 == 0:
                # print("Right here")
                lo = mid + 1
            else:
                hi = mid - 2
        elif nums[mid + 1] == nums[mid]:
            if len(nums[:mid + 2]) % 2 == 0:
                lo = mid + 2
            else:
                hi = mid - 1
        else:
            return nums[mid]

# For testing
n = [1,1,2,3,3]
    # [1,1,2,2,3,3,4,4,5,5,6,7,7,8,8,9,9]

print(singleNonDuplicate(n))
