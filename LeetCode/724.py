"""
@date: 2021/09/06
@desc:  
  The pivot index is the index where the sum of all the numbers strictly to the left of the index 
  is equal to the sum of all the numbers strictly to the index's right.
@key: array
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      t_sum = 0
      for i in range(0, len(nums)):
        t_sum += nums[ i ]

      pivot, l_sum, r_sum = 0,0,0
      while pivot < len(nums):
        r_sum = t_sum - nums[pivot] - l_sum

        if l_sum == r_sum:
          return pivot
        
        l_sum += nums[pivot]
        pivot += 1
     
      return -1



      # l_sum, r_sum = 0, 0
      # for i in range(1, len(nums)):
      #   r_sum += nums[ i ]
      
      # pivot = 0
      # while pivot < len(nums):
      #   if l_sum == r_sum:
      #     return pivot

      #   pivot += 1
      #   if pivot == len(nums):
      #     return -1

      #   l_sum += nums[pivot - 1]
      #   r_sum -= nums[pivot]
      # return -1


assert Solution().pivotIndex([-1,-1,0,1,0,-1]) == 4
assert Solution().pivotIndex([1,7,3,6,5,6]) == 3
assert Solution().pivotIndex([1,2,3]) == -1
assert Solution().pivotIndex([-2,2,3]) == 2
assert Solution().pivotIndex([2,1,-1]) == 0
