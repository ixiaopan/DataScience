"""
@date: 2021/09/08
@desc:
  Given an array of integers numbers that is already sorted in non-decreasing order, 
  find two numbers such that they add up to a specific target number.
@key: two pointer - opposite
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
          t = numbers[l] + numbers[r]
          if t < target:
            l += 1
          elif t > target:
            r -= 1
          else:
            return [ l + 1, r +1 ]
          


assert Solution().twoSum([2,7,11,15], 9)  == [1, 2]
