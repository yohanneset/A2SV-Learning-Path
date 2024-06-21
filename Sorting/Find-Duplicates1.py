# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# using cyclic sort
def find_duplicates(nums):
    i = 0
    duplicates = []
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicates.append(nums[i])
    return duplicates
