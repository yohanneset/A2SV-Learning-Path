# https://leetcode.com/problems/sort-colors/description/
def sortColors(nums):
    i = 0
    j = len(nums) - 1
    k = 0
    while k <= j:
        if nums[k] == 0:
            nums[k], nums[i] = nums[i], nums[k]
            i += 1
            k += 1
        elif nums[k] == 2:
            nums[k], nums[j] = nums[j], nums[k]
            j -= 1
        else:
            k += 1
