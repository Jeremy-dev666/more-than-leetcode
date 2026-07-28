# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, fa, gra):
            nonlocal ans
            if node is None:
                return

            if gra and gra.val % 2 == 0:
                ans += node.val

            dfs(node.left, node, fa)
            dfs(node.right, node, fa)

        ans = 0
        dfs(root, None, None)
        return ans