# https://leetcode.com/problems/range-sum-query-immutable/description/

     
def sumRange(self, left: int, right: int) -> int:
    return sum(self.nums[left:right + 1])