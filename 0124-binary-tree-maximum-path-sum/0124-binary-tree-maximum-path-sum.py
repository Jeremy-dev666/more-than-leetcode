# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # pathsum = l_path + r_path + node.val
        # return max(l_path, r_path) = node.val

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)

            ans = max(ans, l + r + node.val)
            return max(l, r) + node.val

        ans = float('-inf')
        dfs(root)
        return ans