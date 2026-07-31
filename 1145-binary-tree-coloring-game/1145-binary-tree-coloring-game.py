# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        def dfs(node):
            if node is None:
                return 0

            l_cnt = dfs(node.left)
            r_cnt = dfs(node.right)

            # 当遍历到x节点是存一个外部变量
            if node.val == x:
                nonlocal x_l_cnt, x_r_cnt
                x_l_cnt, x_r_cnt = l_cnt, r_cnt

            return l_cnt + r_cnt + 1

        x_l_cnt, x_r_cnt = 0, 0
        dfs(root)
        return max(x_l_cnt, x_r_cnt, n - 1 - x_l_cnt - x_r_cnt) * 2 > n            