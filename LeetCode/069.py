"""
@date: 2021/09/05
@desc:
  sqrt(x)
@key: binary search
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # considering all integers
        # n = 0
        # while n * n <= x:
        #   n += 1
        # return n - 1

        # sorted array
        # n^2 < x, dismiss all values that < n
        # n^2 > x, dismiss all values that > n
        i, j = 0, x
        while i <= j:
          mid = (i + j) // 2
          if mid * mid < x:
            i = mid + 1
          elif mid * mid > x:
            j = mid - 1
          else:
            return mid
        return i - 1


assert Solution().mySqrt(8) == 2
assert Solution().mySqrt(4) == 2
assert Solution().mySqrt(0) == 0
