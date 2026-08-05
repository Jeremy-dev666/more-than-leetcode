# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return (0, True, float('inf'), float('-inf'))

            left_size, left_bst, left_min, left_max = dfs(node.left)
            right_size, right_bst, right_min, right_max = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                total_size = left_size + right_size + 1
                ans = max(ans, total_size)
                # 这里的min(), max()比较是为了排除左右子树为空的情况
                # 因为当子树为空时，min_val = float('inf')，max同理
                return (total_size, True, min(left_min, node.val), max(right_max, node.val))

            return (0, False, float('-inf'), float('inf'))

        ans = 0
        dfs(root)
        return ans