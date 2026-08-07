# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def lca(node):
            if not node or node.val in (p, q):
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            return left or right

        def depth(node, target, d):
            if not node:
                return -1
            if node.val == target:
                return d

            # 先往左子树找，没有再往右子树找
            found = depth(node.left, target, d + 1)
            if found != -1:
                return found
            return depth(node.right, target, d + 1)

        ancestor = lca(root)
        return depth(ancestor, p, 0) + depth(ancestor, q, 0)