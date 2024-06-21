# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# using count sort
def find_duplicates(nums):
    freq = [0] * (len(nums) + 1)
    for x in nums:
        freq[x] += 1
        duplicate = []
    for i in range(len(freq)):
        if freq[i] == 2:
            duplicate.append(i)
            return duplicate
