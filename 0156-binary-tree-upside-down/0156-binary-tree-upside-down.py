# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        cur = root
        prev_root = None
        prev_right = None

        while cur:
            nxt = cur.left
            cur_right = cur.right
            cur.left = prev_right
            cur.right = prev_root

            prev_root = cur
            prev_right = cur_right
            cur = nxt

        return prev_root