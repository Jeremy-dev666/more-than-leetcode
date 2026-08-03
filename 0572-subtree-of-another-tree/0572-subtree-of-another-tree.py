# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        # 遍历主树的每一个节点去尝试和subRoot子树比较
        def dfs(node):
            if node is None:
                return False
            if isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)