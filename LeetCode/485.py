"""
@date: 2021/09/08
@dec:
  Given a binary array nums, return the maximum number of consecutive 1's in the array.
@key: array
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      cnt,max_cnt = 0,0
      for n in nums:
        if n == 1:
          cnt += 1
          max_cnt = max(max_cnt, cnt)
        else:
          cnt = 0
  
      return max_cnt

 
assert Solution().findMaxConsecutiveOnes([0,0]) == 0
assert Solution().findMaxConsecutiveOnes([1,1,1,1]) == 4
assert Solution().findMaxConsecutiveOnes([1,0]) == 1
assert Solution().findMaxConsecutiveOnes([1,0,1]) == 1
assert Solution().findMaxConsecutiveOnes([0,1,1]) == 2
assert Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3

      

