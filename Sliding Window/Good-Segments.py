# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/D


def good_segment(arr, k, n):
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    count = j = 0

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    for i in range(n):
        while prefix_sum[i] >= k:
            prefix_sum[i] -= arr[j]
            j += 1
            count += 1
    return count


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(good_segment(arr, k, n))
