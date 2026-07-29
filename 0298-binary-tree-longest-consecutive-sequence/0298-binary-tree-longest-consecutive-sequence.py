# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, prev_val, length):
            nonlocal ans

            if node is None:
                return

            if node.val == prev_val + 1:
                length += 1
            else:
                length = 1
            ans = max(ans, length)

            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)

        ans = 0
        dfs(root, root.val - 1, 0)
        return ans