"""
@date: 2021/08/31
@desc:
  Given an integer x, return true if x is palindrome integer.
  An integer is a palindrome when it reads the same backward as forward. 
  - For example, 121 is palindrome while 123 is not.
  - Constraints: reversing_x \in [-2^31, 2^31 - 1], othewise return 0.
@key: math
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
      # negative numbers => No
      # multiple of 10, excluding 0 => No
      if x < 0 or (x != 0 and x % 10 == 0):
        return False

      if x < 10: # one-digit numbers => Yes
        return True

      MAX_VAL = 2**31 - 1 # 2147483647

      copy_x = x
      reversed_x = 0
      while copy_x > 0:
        mod_x = copy_x % 10
        copy_x = copy_x // 10

        if reversed_x * 10 + mod_x > MAX_VAL:
          return False
        
        reversed_x = reversed_x * 10 + mod_x
  
        if reversed_x > copy_x:
          return False

        if reversed_x == copy_x or reversed_x == copy_x // 10:
          return True


assert Solution().isPalindrome(0) == True
assert Solution().isPalindrome(121) == True
assert Solution().isPalindrome(-121) == False
assert Solution().isPalindrome(10) == False
assert Solution().isPalindrome(-101) == False
