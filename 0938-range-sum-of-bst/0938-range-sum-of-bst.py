# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            nonlocal ans
            if node is None:
                return
            
            if node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            else:
                ans += node.val
                dfs(node.left)
                dfs(node.right)

        ans = 0
        dfs(root)
        return ans