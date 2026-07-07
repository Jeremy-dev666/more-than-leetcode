# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            # 递归存一堆元组信息（抢或不抢的价值）
            if node is None:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)

            # 子树都不抢，那么父节点价值可以算上
            par_rob = node.val + l_not_rob + r_not_rob
            # 子树有一个抢，那么父节点就不能抢
            par_not = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)

            return par_rob, par_not

        return max(dfs(root))
