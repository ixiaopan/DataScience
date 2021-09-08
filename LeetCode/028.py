"""
@date: 2021/09/03
@desc
  Return the index of the first occurrence of needle in haystack, 
  or -1 if needle is not part of haystack.
@key: string match
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None or needle == haystack:
          return 0
       
        if haystack is None :
          return -1

        m = len(haystack)
        n = len(needle)
        for i in range(m - n + 1):
          if haystack[i : i + n] == needle:
            return i
        return -1

# 
assert Solution().strStr('hellop', 'lla') == -1
assert Solution().strStr('aaaa', 'bba') == -1
assert Solution().strStr('', '') == 0
assert Solution().strStr('cc', 'a') == -1
assert Solution().strStr('mississippi', 'issip') == 4