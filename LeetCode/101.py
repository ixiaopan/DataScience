"""
@date: 2021/09/10
@desc: Symmetric tree
@key: tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [ root ]
        while len(queue) > 0:
            next_level = []
            next_level_val = []
            for n in queue:
                next_level += [ n.left, n.right ]
                if n.left:
                    next_level_val.append( n.left.val )
                else:
                    next_level_val.append('')
                if n.right:
                    next_level_val.append( n.right.val )
                else:
                    next_level_val.append('')
   
            mid = len(next_level) // 2
            if next_level_val[ :mid ] != next_level_val[ :(mid - 1):-1 ]:
                return False            
            
            queue = [ n for n in next_level if n ]
        
        return True
