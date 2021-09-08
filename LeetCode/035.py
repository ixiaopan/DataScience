"""
@date: 2021/09/04
@desc
  Given a sorted array of distinct integers and a target value, return the index if the target is found. 
  If not, return the index where it would be if it were inserted in order.
@key: binary search
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
          mid = (i + j) // 2
          if target > nums[ mid ]:
            i = mid + 1
          elif target < nums[ mid] :
            j = mid - 1
          else:
            return mid

        return i


assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert([1,3,5,6], 2) == 1
assert Solution().searchInsert([1,3,5,6], 7) == 4
assert Solution().searchInsert([1,3,5,6], 0) == 0
assert Solution().searchInsert([1], 0) == 0
assert Solution().searchInsert([1, 3], 2) == 1