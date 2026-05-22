# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -math.inf
        self.dfs(root)
        return self.ans

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_val = max(self.dfs(node.left), 0)
        right_val = max(self.dfs(node.right), 0)
        max_sum = left_val + right_val + node.val
        self.ans = max(self.ans, max_sum)

        return node.val + max(left_val, right_val)