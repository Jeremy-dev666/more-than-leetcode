# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        # 自顶向下一路探到叶子节点（那么由此保证了祖先孙子关系）
        # 探路过程中维护最大值、最小值（包括当前节点值作比较）
        # 当到达叶子节点时更新答案
        def dfs(node, cur_max, cur_min):
            if node is None:
                return cur_max - cur_min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            return max(dfs(node.left, cur_max, cur_min), dfs(node.right, cur_max, cur_min))

        return dfs(root, root.val, root.val)

            