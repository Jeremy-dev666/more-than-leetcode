# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0

            # 节点不为空，本身自己贡献 1, 1
            incr, decr = 1, 1

            if node.left:
                l_incr, l_decr = dfs(node.left)
                if node.left.val == node.val + 1:
                    incr = l_incr + 1
                elif node.left.val == node.val - 1:
                    decr = l_decr + 1

            if node.right:
                r_incr, r_decr = dfs(node.right)
                if node.right.val == node.val + 1:
                    # 左右都是递增取其一
                    incr = max(incr, r_incr + 1)
                elif node.right.val == node.val - 1:
                    decr = max(decr, r_decr + 1)

            ans = max(ans, incr + decr - 1)
            return incr, decr

        ans = 0
        dfs(root)
        return ans