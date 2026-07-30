# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False

            return dfs(p.left, q.right) and dfs(p.right, q.left) or dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(root1, root2)
