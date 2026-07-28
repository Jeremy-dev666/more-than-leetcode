# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, max_num, min_num):
            nonlocal ans
            if node is None:
                return

            abs_val = max(abs(node.val - max_num), abs(node.val - min_num))
            ans = max(abs_val, ans)

            max_num = max(max_num, node.val)
            min_num = min(min_num, node.val)

            dfs(node.left, max_num, min_num)
            dfs(node.right, max_num, min_num)

        ans = -1
        dfs(root, root.val, root.val)
        return ans