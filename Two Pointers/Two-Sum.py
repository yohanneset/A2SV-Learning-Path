# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i <= j:
        sum = numbers[i] + numbers[j]
        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            return [i + 1, j + 1]
