# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, num):
            nonlocal ans
            if node is None:
                return 

            num = num * 10 + node.val

            if node.left is None and node.right is None:
                ans += num

            dfs(node.left, num)
            dfs(node.right, num)

        ans = 0
        dfs(root, 0)
        return ans