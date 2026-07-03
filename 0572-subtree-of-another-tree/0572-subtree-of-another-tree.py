# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_height = self._getH(subRoot)

        # postorder traversal, and return Tuple[height, isFound]
        def dfs(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if node is None:
                return 0, False

            l_h, l_found = dfs(node.left)
            r_h, r_found = dfs(node.right)
            # 如果子树已经找到匹配，那么直接上传信号，无需再通过高度剪枝
            if l_found or r_found:
                return 0, True

            # 比较高度来进行isSame方法调用的剪枝
            node_h = max(l_h, r_h) + 1
            return node_h, node_h == sub_height and self._isSame(node, subRoot)

        return dfs(root)[1]

    def _getH(self, node):
        if node is None:
            return 0
        return max(self._getH(node.left), self._getH(node.right)) + 1

    def _isSame(self, t1, t2):
        if t1 is None or t2 is None:
            return t1 is t2
        return t1.val == t2.val and \
            self._isSame(t1.left, t2.left) and \
            self._isSame(t1.right, t2.right)