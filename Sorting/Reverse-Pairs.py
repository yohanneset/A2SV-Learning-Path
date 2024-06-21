# https://leetcode.com/problems/reverse-pairs/
def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]


def merge_sort(nums, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid + 1, high)
    merge(nums, low, mid, high)


def reverse_pairs(nums):
    merge_sort(nums, 0, len(nums) - 1)
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > 2 * nums[i]:
                count += 1
    return count
