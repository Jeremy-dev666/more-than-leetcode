# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        # find in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # find in right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # when val == key, find the largest val in left subtree or smallest val in right subtree
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            ptr = root.left
            while ptr.right:
                ptr = ptr.right
            root.val = ptr.val
            root.left = self.deleteNode(root.left, ptr.val)

        return root