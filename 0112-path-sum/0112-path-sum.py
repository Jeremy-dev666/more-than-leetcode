# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, target):
            if node is None:
                return False

            if node.left is None and node.right is None and target == node.val:
                return True

            target -= node.val
            return dfs(node.left, target) or dfs(node.right, target)

        return dfs(root, targetSum)