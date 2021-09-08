class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # l,r = len(a) - 1, len(b) - 1
        # if l < r:
        #   a = abs(r - l)*'0' + a
        # elif r < l:
        #   b = abs(r - l)*'0' + b
        # l,r = len(a) - 1, len(b) - 1


        # val = ''
        # inc = 0
        # while l>=0 and r >=0:
        #   v_a = int( a[l] )
        #   v_b = int( b[r] )
          
        #   s = v_a + v_b + inc
        #   val = str(s % 2) + val
        #   if s == 2:
        #     inc = 1
        #   else:
        #     inc = 0
        #   l-=1 
        #   r-=1

        # if inc == 1:
        #   val = '1' + val
        
        # return val



        l,r = len(a) - 1, len(b) - 1
        pre_sum = 0
        val = ''
        while l >=0 or r >= 0 or pre_sum:
          if l>=0:
            pre_sum += int(a[l])
            l -= 1

          if r>=0:
            pre_sum += int(b[r])
            r -= 1

          val += str(pre_sum % 2)
          pre_sum = pre_sum // 2

        return val[::-1]

assert Solution().addBinary('10', '1') == '11'
assert Solution().addBinary('11', '1') == '100'
assert Solution().addBinary('1010', '1011') == '10101'
        
