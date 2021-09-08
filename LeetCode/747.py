"""
@date: 2021/09/06
@desc:  
  Given an integer array nums where the largest integer is unique.
  Determine whether the largest element in the array is at least twice as much as every other number in the array. 
  If it is, return the index of the largest element, or return -1 otherwise.
@key: array
"""

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
      max_val, second_max_val = -99, -99
      max_index = -1
      for i in range(0, len(nums)):
        if nums[i] > max_val:
          second_max_val = max_val
          max_val = nums[i]
          max_index = i
        elif nums[i] > second_max_val:
          second_max_val = nums[i]

      if max_val < second_max_val * 2:
        return -1

      return max_index



      max_index = 0
      for i in range(0, len(nums)):
        if nums[i] >= nums[ max_index ]:
          max_index = i

      for i in range(0, len(nums)):
        if i == max_index:
          continue
        
        if nums[ max_index ] < 2 * nums[i]:
          return -1
      
      return max_index



assert Solution().dominantIndex([3,0,0,2]) == -1
assert Solution().dominantIndex([0,0,3,2]) == -1
assert Solution().dominantIndex([1]) == 0
assert Solution().dominantIndex([3,6,1,0]) == 1
assert Solution().dominantIndex([1,2,3,4]) == -1
