"""
@date: 2021/09/09
@desc:
  Since each version is developed based on the previous version, 
  all the versions after a bad version are also bad.
@key: binary search
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version, pick):
  return not version < pick


class Solution:
    def firstBadVersion(self, n, pick):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
          mid = (l+r)//2
          if isBadVersion(mid, pick) is False:
            l = mid + 1
          else:
            r = mid

        # if l <= n and isBadVersion(l, pick) is True:
        return l

        # return -1

assert Solution().firstBadVersion(5, 4) == 4
assert Solution().firstBadVersion(1,1) == 1
assert Solution().firstBadVersion(5,5) == 5
        