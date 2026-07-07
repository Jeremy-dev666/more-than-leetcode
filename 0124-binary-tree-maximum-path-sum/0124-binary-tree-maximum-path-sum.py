# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 两件事：1.更新当前能获得的最大值， 2.决定向上传递值（左右子树只能选一边或不选）
        ans = -float('inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)

            max_sum = left_val + right_val + node.val
            ans = max(ans, max_sum)

            return node.val + max(left_val, right_val)

        dfs(root)
        return ans
