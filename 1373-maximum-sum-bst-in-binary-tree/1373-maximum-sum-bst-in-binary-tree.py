# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            # 空节点初始化为极值
            if node is None:
                return inf, -inf, 0

            l_min, l_max, l_sum = dfs(node.left)  # 递归左子树
            r_min, r_max, r_sum = dfs(node.right)  # 递归右子树

            # 先判断当前是否为二叉搜索树
            if node.val <= l_max or node.val >= r_min:
                return -inf, inf, 0

            total = l_sum + r_sum + node.val
            self.ans = max(self.ans, total)
            
            # 和inf, -inf比较，防止空节点
            return min(l_min, node.val), max(r_max, node.val), total

        dfs(root)
        return self.ans