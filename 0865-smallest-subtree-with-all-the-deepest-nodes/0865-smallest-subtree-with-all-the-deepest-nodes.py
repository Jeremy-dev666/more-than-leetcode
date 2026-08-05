# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return (None, 0)  # (node, depth)

            left_ans, left_depth = dfs(node.left)
            right_ans, right_depth = dfs(node.right)

            if left_depth == right_depth:
                return (node, left_depth + 1)
            else:
                return (left_ans, left_depth + 1) if left_depth > right_depth else (right_ans, right_depth + 1)

        ans, depth = dfs(root)
        return ans

            