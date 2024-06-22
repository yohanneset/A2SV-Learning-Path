# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
nums = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = [0] * m
i = j = 0

while i < n and j < m:
    if nums[i] < arr[j]:
        i += 1
    else:
        result[j] = i
        j += 1
while j < m:
    result[j] = i
    j += 1

print(result)
