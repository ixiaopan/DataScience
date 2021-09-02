"""
@date: 2021/09/02
@desc
 Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
 The relative order of the elements may be changed.

@key: two pointer approach
    https://towardsdatascience.com/two-pointer-approach-python-code-f3986b602640
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      # opposite direction
      # start = 0
      # end = len(nums) - 1
      # while start <= end:
      #   if nums[start] == val:
      #     while end >= 0 and nums[end] == val:
      #       end -= 1
          
      #     if end <= start:
      #       break

      #     nums[end], nums[start] = nums[start], nums[end]

      #   start += 1

      # return start

      # the same direction
      # j - slow runner (indicate the first k)
      # i - fast runner (loop each element)
      i,j = 0,0
      while i < len(nums):
        if nums[i] != val:
          nums[j] = nums[i]
          i += 1
          j += 1
        else:
          i += 1
      
      return j

assert Solution().removeElement([3, 2, 2, 3], 3) == 2
assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert Solution().removeElement([1, 1, 1], 1) == 0
assert Solution().removeElement([1], 1) == 0

