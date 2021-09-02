"""
@date: 2021/09/02
@desc
 Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
 The relative order of the elements should be kept the same.

@key: two pointer approach
    https://towardsdatascience.com/two-pointer-approach-python-code-f3986b602640
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 1
        n = len(nums)

        while end < n:
          if nums[end] == nums[start]:
            end += 1
          elif end - start == 1:
            start += 1
            end += 1
          else:
            nums[start + 1], nums[ end ] = nums[ end ], nums[start + 1]
            start += 1
            end += 1

        return start + 1


def check(nums, expectedNums):
  k = Solution().removeDuplicates(nums)

  assert k == len(expectedNums)
  for i in range(k):
    assert nums[i] == expectedNums[i]

check([1, 2, 3], [1, 2, 3])
check([1, 1, 2, 3], [1, 2, 3])
check([1, 1, 2], [1, 2])
check([0,0,1,1,1,2,2,3,3,4], [0, 1, 2, 3, 4])
