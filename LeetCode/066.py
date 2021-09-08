"""
@date: 2021/09/05
@desc:
  You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
  The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
  Increment the large integer by one and return the resulting array of digits.
@key: math
"""

class Solution:
    def plusOne(self, digits):
        # l_arr = []
        # r_arr = []
        # incr = 1
        # for i in range( len(digits) - 1, -1, -1):
        #   d = digits[i]
          
        #   next_d = (d + incr) % 10
        #   r_arr.insert(0, next_d)
        #   if next_d == 0:
        #     incr = 1
        #   else:
        #     l_arr = digits[:i]
        #     incr = 0
        #     break
        
        # if incr == 1 and len(digits) == len(r_arr):
        #   l_arr = [1]

        # return l_arr + r_arr

        if not digits:
          return [1]

        new_d = (digits[-1] + 1) % 10
        if new_d == 0:
          return self.plusOne( digits[:-1] ) + [ new_d ]        
        else:
          digits[-1] = new_d
          return digits

assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]
assert Solution().plusOne([0]) == [1]
assert Solution().plusOne([9,9]) == [1,0,0]
assert Solution().plusOne([9]) == [1,0]