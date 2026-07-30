# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 自底向上返回节点高度（子树高度信息）
        # -999 作为不平衡树的信号标记
        def dfs(node):
            if node is None:
                return 0

            left_tree = dfs(node.left)
            if left_tree == -999:  # 不平衡树提前剪枝
                return -999
            right_tree = dfs(node.right)
            if right_tree == -999: # 不平衡树提前剪枝
                return -999
            if abs(left_tree - right_tree) > 1:
                return -999

            return 1 + max(left_tree, right_tree)

        return dfs(root) != -999

            
