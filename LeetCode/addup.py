import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
nums = [ int(i) for i in input().split() ]

def get_next(nums, next_add=None):
    if next_add is not None:
        nums = nums[2:] + [ next_add ]

    nums = sorted(nums)    
    
    return nums, nums[0]+nums[1]

cost = 0
next_add = 0
for i in range(n-1): 
    if i == 0:
        nums, next_add = get_next(nums)
    else:
        nums, next_add = get_next(nums, next_add)
    cost += next_add


print(cost)
