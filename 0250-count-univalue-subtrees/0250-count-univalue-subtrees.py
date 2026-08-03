# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def isUni(node):
            nonlocal ans
            if not node:
                return True

            left = isUni(node.left)
            right = isUni(node.right)

            # 1.左右子树有一个不是同值树，直接向上传递False
            if not left or not right:
                return False
            # 2.左右子树都是同值树，那么和当前节点比较
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False

            ans += 1
            return True

        ans = 0
        isUni(root)
        return ans