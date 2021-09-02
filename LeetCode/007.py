"""
@date: 2021/08/31
@desc:
  Given a signed 32-bit integer x, return x with its digits reversed.
  Constraints: reversing_x \in [-2^31, 2^31 - 1], othewise return 0.
@key: math
"""

class Solution:
    def reverse(self, x: int) -> int:
      if x == 0:
        return 0

      MAX_VAL = 2**31 - 1 # 2147483647
      abs_x = abs(x)
      reverse_x = 0
      while abs_x != 0:
        mod_x = abs_x % 10
        abs_x = abs_x // 10

        if reverse_x * 10 + mod_x > MAX_VAL:
          return 0

        reverse_x = reverse_x * 10 + mod_x

      return int(x / abs(x)) * reverse_x


assert Solution().reverse(0) == 0
assert Solution().reverse(-2147483647) == 0
assert Solution().reverse(239999999999) == 0
