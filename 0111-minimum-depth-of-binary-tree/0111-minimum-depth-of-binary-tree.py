# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return 0

            if node.left and node.right:
                return min(dfs(node.left), dfs(node.right)) + 1
            
            else:
                # 当只有一个孩子或者都没有，就不需要比较，自然返回有值的那个就好
                return dfs(node.left) + dfs(node.right) + 1

        return dfs(root)
            