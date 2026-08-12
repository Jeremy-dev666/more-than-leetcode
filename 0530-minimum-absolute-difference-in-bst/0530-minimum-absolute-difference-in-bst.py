# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序遍历可以让数组有序，最小差值为相邻两数的差值
        self.prev = -inf
        def dfs(node):
            nonlocal ans
            if node is None:
                return 
            
            dfs(node.left)
            # 中序遍历
            ans = min(ans, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)

        ans = inf
        dfs(root)
        return ans

