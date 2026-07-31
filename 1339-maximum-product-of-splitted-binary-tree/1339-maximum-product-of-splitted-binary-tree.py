# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        # 1. 算出整棵树的总和
        total = 0
        def dfs(node):
            nonlocal total
            if node is None:
                return
            total += node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        # 2. 自底向上返回，获取到当前节点 为根 的树 节点值总和，就可以知道断裂的另一棵
        ans = 0
        def find(node):
            nonlocal ans
            if node is None:
                return 0

            cur_sum = find(node.left) + find(node.right) + node.val
            ans = max(ans, cur_sum * (total - cur_sum))

            return cur_sum

        find(root)
        MOD = 10**9 + 7
        return ans % MOD
