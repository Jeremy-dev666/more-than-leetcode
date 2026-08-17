# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(left_node, right_node, is_odd):
            if not left_node:
                return
            if is_odd:
                left_node.val, right_node.val = right_node.val, left_node.val
            dfs(left_node.left, right_node.right, not is_odd)
            dfs(left_node.right, right_node.left, not is_odd)

        if root:
            dfs(root.left, root.right, True)
        return root