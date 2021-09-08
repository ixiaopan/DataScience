"""
@date: 2021/09/05
@desc
  Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
  A word is a maximal substring consisting of non-space characters only.
@key: string
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split()[-1]
        return len(last_word)

assert Solution().lengthOfLastWord('a') == 1
assert Solution().lengthOfLastWord('a b') == 1