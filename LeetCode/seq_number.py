
from collections import Counter

def findNumber(n, m, num):
    '''
    n: threshold [1, n]
    m, the first m numbers
    num: a sequence of numbers split by space
       e.g. 1 2 2 3
    '''
    counter = Counter(num)

    ret = []
    for i in range(m):
      min_c = 2*m + 1
      min_v = n + 1

      for (v, c) in counter.most_common()[::-1]:
        if c < min_c:
          min_c = c
          min_v = v
        elif c == min_c:
          min_v = min(min_v, v)
        else:
          break

      ret.append(min_v)
      counter.update([min_v])
    
    return ret

assert findNumber(3, 4, [1, 2, 2, 3]) == [1, 3, 1, 2]
assert findNumber(3, 4, [1, 2, 2, 1, 3]) == [3, 1, 2, 3]
