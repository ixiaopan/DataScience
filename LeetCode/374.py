"""
@date: 2021/09/08
@desc:
  I pick a number from 1 to n. You have to guess which number I picked.
  -1: The number I picked is lower than your guess (i.e. pick < num).
  1: The number I picked is higher than your guess (i.e. pick > num).
  0: The number I picked is equal to your guess (i.e. pick == num).
@key: binary search
"""



def guess(num: int, pick: int) -> int:
  if pick < num:
    return -1
  if pick > num:
    return 1
  return 0

class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
      i, j = 1, n
      while i <= j:
        mid = ( i + j ) // 2
        ret = guess(mid, pick)
        if ret > 0:
          i = mid + 1
        elif ret < 0:
          j = mid - 1
        else:
          return mid


assert Solution().guessNumber(10, 6) == 6
assert Solution().guessNumber(1, 1) == 1
assert Solution().guessNumber(2, 2) == 2
assert Solution().guessNumber(12, 8) == 8
 