"""
@date: 2021/09/05
@desc:
  Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
@key: two pointer approach
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) ==  0:
          return False
        
        l, r = 0, len(s) - 1
        isValid = True
        while l <= r:
          while l <= r and not s[l].lower().isalnum():
            l += 1
          
          while l <= r and not s[r].lower().isalnum():
            r -= 1

          if l <= r and s[l].lower() == s[r].lower():
            l += 1 
            r -= 1
          else:
            isValid = False
            break

        return isValid
        

assert Solution().isPalindrome(' ') == False
assert Solution().isPalindrome('') == False
assert Solution().isPalindrome('s') == True
assert Solution().isPalindrome('ssas') == False
assert Solution().isPalindrome('race a car') == False
assert Solution().isPalindrome('A man, a plan, a canal: Panama') == True
