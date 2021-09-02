"""
@date: 2021/09/02
@desc
  Write a function to find the longest common prefix string amongst an array of strings. 
  If there is no common prefix, return an empty string "".

@key: string match
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #   return ''
        # par_pre = ''
        # prefix = strs[0]
        # i = 0
        # while i < len(prefix):
        #   end = False
        #   for str in strs[1:]:
        #     if i >= len(str) or str[i] != prefix[i]:
        #       end = True
        #       break
          
        #   if end:
        #     break

        #   i += 1
        #   par_pre = prefix[:i]

        # return par_pre


        if len(strs) == 0:
          return ''

        prefix = strs[0]
        for str in strs[1:]:
          match = -1
          while match != 0:
            try:
              match = str.index(prefix)
            except:
              match = -1

            if match != 0:
              prefix = prefix[:-1]
          
          if not prefix:
            break
        
        return prefix
          

assert Solution().longestCommonPrefix(["flower","flow","flight"]) == 'fl'
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ''
assert Solution().longestCommonPrefix(["car","car","car"]) == 'car'
assert Solution().longestCommonPrefix([]) == ''
assert Solution().longestCommonPrefix(["c","acc","ccc"]) == ''