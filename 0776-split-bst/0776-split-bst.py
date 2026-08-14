# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        # xs, xl --->  小于等于target的树，大于target的树
        if root is None:
            return [None, None]

        # <= target:那么左子树必然都<=target，右子树的左节点可能有<=target的，需继续探索
        if root.val <= target:
            xs, xl = self.splitBST(root.right, target)
            root.right = xs
            return [root, xl]
        else:
            xs, xl = self.splitBST(root.left, target)
            root.left = xl
            return [xs, root]
