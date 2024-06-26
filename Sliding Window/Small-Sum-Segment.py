# https://codeforces.com/edu/course/2/lesson/9/2/practice
n, k = map(int, input().split())
arr = list(map(int, input().split()))


def small_sum(arr, k, n):
    i = sum = j = 0
    res = 0
    for i in range(n):
        sum += arr[i]
        while sum > k:
            sum -= arr[j]
            j += 1
        res = max(res, i - j + 1)
    return res


print(small_sum(arr, k, n))
