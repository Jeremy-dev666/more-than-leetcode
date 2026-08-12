# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev = -inf
        def dfs(node):
            nonlocal ans, prev
            if node is None:
                return

            dfs(node.left)
            ans = min(ans, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return ans