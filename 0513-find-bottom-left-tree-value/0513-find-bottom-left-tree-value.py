# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 按题意：最后一行的第一个元素

        self.max_depth = -1
        self.ans = root.val

        def dfs(node, depth):
            if node is None:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.ans
        