# https://codeforces.com/problemset/problem/977/C
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


def less_or_equal(nums, k):
    merge_sort(nums, 0, len(nums) - 1)
    if nums[k - 1] + 1 < nums[k]:
        return nums[k - 1] + 1
    else:
        return -1
