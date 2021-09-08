"""
@date: 2021/09/05
@desc:
  You are given two integer arrays nums1 and nums2, 
  sorted in non-decreasing order, 
  and two integers m and n, 
  representing the number of elements in nums1 and nums2 respectively.
@key: two pointer - same
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        e = m + n
        while m > 0 and n > 0:
          if nums1[ m - 1 ] > nums2[ n - 1 ]:
            nums1[ e - 1] = nums1[ m - 1 ]
            m -= 1
          else:
            nums1[ e - 1 ] = nums2[ n - 1 ]
            n -= 1
          e -= 1
        
        if n > 0:
          nums1[:e] = nums2[:n]
        return nums1


assert Solution().merge([1,2,3,0,0,0],3, [2, 5, 6], 3) == [1,2,2,3,5,6]
assert Solution().merge( [2, 5, 6,0,0,0], 3, [1,2,3],3) == [1,2,2,3,5,6]
assert Solution().merge([1],1, [], 0) == [1]
assert Solution().merge([0],0, [1], 1) == [1]
