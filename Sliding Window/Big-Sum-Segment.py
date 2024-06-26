# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/B
n, k = map(int, input().split())
arr = list(map(int, input().split()))


def big_sum(arr, k, n):
    i = sum = j = 0
    res = n + 1
    for i in range(n):
        sum += arr[i]
        while sum - arr[j] > k:
            sum -= arr[j]
            j += 1
        if sum >= k:
            res = min(i - j + 1, res)
    return res if res != n + 1 else -1


print(big_sum(arr, k, n))
