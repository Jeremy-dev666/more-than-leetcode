# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_flag = False
        self.q_flag = False

        def dfs(node):
            if node is None:
                return None

            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == p.val:
                self.p_flag = True  # 后序遍历标记p, q是否存在
                return node    # 同时记录lca节点
            if node.val == q.val:
                self.q_flag = True  # 后序遍历标记p, q是否存在
                return node    # 同时记录lca节点
            if l and r:
                return node    # 同时记录lca节点
            return l or r

        lca = dfs(root)
        if self.p_flag and self.q_flag:
            return lca
        return None