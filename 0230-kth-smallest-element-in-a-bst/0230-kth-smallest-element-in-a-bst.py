# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        def dfs(node):
            nonlocal ans
            if node is None:
                return

            dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                ans = node.val
                return
            dfs(node.right)

        ans = -1
        dfs(root)
        return ans