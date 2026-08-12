# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return True
            if not dfs(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return dfs(node.right)
        
        self.prev = float('-inf')
        return dfs(root)