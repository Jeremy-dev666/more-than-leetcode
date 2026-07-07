# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # 递归遍历，如果左右子节点为空（说明是叶子节点）
        # 且当前节点值==目标值那么可以删除，返回None
        if not root.left and not root.right and root.val == target:
            return None
        # 否则返回当前节点
        return root