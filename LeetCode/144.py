"""
@date: 2021/09/10
@desc:
  Binary Tree Preorder Traversal
@key: tree
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
          return []
        
        # recursive
        # l_n = self.preorderTraversal(root.left)
        # r_n = self.preorderTraversal(root.right)
        # return [ root.val ]  + l_n + r_n

        # iteratively
        val = []
        stack = [ root ]
        while len(stack) > 0:
          node = stack.pop()
          val.append( node.val )

          if node.right:
            stack.append( node.right )
          
          if node.left:
            stack.append( node.left )
        return val


A = TreeNode(2)
A.left = TreeNode(3)
tree = TreeNode(1, None, A)
assert Solution().preorderTraversal(tree) == [1, 2, 3]
A = TreeNode(2)
tree = TreeNode(1, A, None)
assert Solution().preorderTraversal(tree) == [1, 2]