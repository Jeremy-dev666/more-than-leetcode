# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            # 后序遍历，如果子树跟当前节点能接的上就长度+1，否则重置为0
            l = l + 1 if node.left and node.left.val == node.val else 0
            r = r + 1 if node.right and node.right.val == node.val else 0

            ans = max(ans, l + r)
            return max(l, r)

        ans = 0
        dfs(root)
        return ans
