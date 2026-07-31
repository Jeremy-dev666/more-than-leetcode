# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # 计算树和、计算树节点数量

        def dfs(node):
            nonlocal ans
            if node is None:
                return (0, 0)

            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            node_sum = left_sum + right_sum + node.val
            node_cnt = left_cnt + right_cnt + 1

            if node.val == node_sum // node_cnt:
                ans += 1

            return (node_sum, node_cnt)

        ans = 0
        dfs(root)
        return ans