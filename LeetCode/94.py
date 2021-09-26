"""
@date: 2021/09/10
@desc:
  Binary Tree Inorder Traversal
@key: tree
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
          return []
        
        # recursive
        # l_n = self.inorderTraversal(root.left)
        # r_n = self.inorderTraversal(root.right)
        # return l_n + [ root.val ] + r_n

        # iteratively
        stack = []
        val = []
        while True:
          while root:
            stack.append(root)
            root = root.left

          if len(stack) == 0:
            return val
         
          # once end, it must be the local root node without left children
          # then we pop it out to visit this node
          # next we visit its right child
          # if the right child is None, we pop up its parent node
          node = stack.pop()
          val.append(node.val)
          root = node.right




A = TreeNode(2)
A.left = TreeNode(3)
tree = TreeNode(1, None, A)
assert Solution().inorderTraversal(tree) == [1, 3, 2]
A = TreeNode(2)
tree = TreeNode(1, A, None)
assert Solution().inorderTraversal(tree) == [2, 1]