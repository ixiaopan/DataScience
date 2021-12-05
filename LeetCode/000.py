# """
# @date: 2021/08/31
# @key: hash table
# """
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range( len(nums) ):
        #   for j in range( i+1, len(nums) ):
        #     if nums[i] + nums[j] == target:
        #       return [i, j]


        hashmap = {}
        for i in range( len(nums) ):
          if nums[i] not in hashmap:
            hashmap[  target - nums[i] ] = i
          else:
            return [ hashmap[ nums[i] ], i ]

assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]



