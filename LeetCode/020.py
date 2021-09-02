"""
@date: 2021/09/02
@desc
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
  An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
@key: stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pair_brackets = {
          '(': ')',
          '[': ']',
          '{': '}'
        }

        if len(s) % 2 != 0: # odd length
          return False

        stack = []
        for e in s:
          if e in pair_brackets.keys():
            stack.append(e)
          
          # closed must be the corresponding symbol
          elif len(stack) and e in pair_brackets.values() and e == pair_brackets[ stack[-1] ]:
            stack = stack[:-1]
          else:
            return False

        return len(stack) == 0



assert Solution().isValid('(') == False
assert Solution().isValid(']') == False
assert Solution().isValid('((((') == False
assert Solution().isValid('[]]]') == False
assert Solution().isValid('()[]{') == False
assert Solution().isValid('([)]') == False
assert Solution().isValid('(]') == False
assert Solution().isValid('()') == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid('{[]}') == True
assert Solution().isValid('[](]') == False
