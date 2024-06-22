# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
nums = list(map(int, input().split()))
arr = list(map(int, input().split()))

i = j = 0
sorted = []
while i < n and j < m:
    if nums[i] <= arr[j]:
        sorted.append(nums[i])
        i += 1
    else:
        sorted.append(arr[j])
        j += 1
while i < n:
    sorted.append(nums[i])
    i += 1
while j < m:
    sorted.append(arr[j])
    j += 1

print(sorted)
