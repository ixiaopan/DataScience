"""
@date: 2021/0909
@desc:
@key: binary search
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      l, r = 0, len(nums) - 1

