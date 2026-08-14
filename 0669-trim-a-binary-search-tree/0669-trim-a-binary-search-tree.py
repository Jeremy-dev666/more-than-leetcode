# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # 如果当前节点值小于low，那么当前节点及它的左子树都可以直接丢弃，右子树修剪
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 大于high同理
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 在范围内左右子树继续遍历
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
            