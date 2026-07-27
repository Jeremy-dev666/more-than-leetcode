# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect(node, ans):
            if node is None:
                return
            if node.left is None and node.right is None:
                ans.append(node.val)
            collect(node.left, ans)
            collect(node.right, ans)

        a1, a2 = [], []
        collect(root1, a1)
        collect(root2, a2)

        return a1 == a2