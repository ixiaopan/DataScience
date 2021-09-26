"""
@date: 2021/09/10
@desc: BFS
@key: tree
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []

        ret = []
        queue = [ root ]
        while len(queue) > 0:
          ret.append( [ n.val for n in queue ] )
        
          next_level = []
          for n in queue:
            next_level += [ n.left, n.right ] 

          queue = [ n for n in next_level if n ]
