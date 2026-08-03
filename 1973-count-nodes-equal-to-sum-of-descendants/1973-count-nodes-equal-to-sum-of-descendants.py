# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left + right == node.val:
                ans += 1

            return left + right + node.val

        ans = 0
        dfs(root)
        return ans