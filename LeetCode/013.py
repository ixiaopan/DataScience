"""
@date: 2021/09/02
@desc:
@key: hash table
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }

        val = 0
        prev_v = 0
        sign = 1
        for e in reversed(s):
          cur_v = roman_int_map[ e ]

          if sign == -1 or cur_v >= prev_v:
            sign = 1
          else:
            sign = -1
          
          val += sign * cur_v
          prev_v = cur_v

        return val

assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("IV") == 4
assert Solution().romanToInt("IX") == 9
assert Solution().romanToInt("LVIII") == 58
assert Solution().romanToInt("MCMXCIV") == 1994
assert Solution().romanToInt("CMLXXX") == 980

