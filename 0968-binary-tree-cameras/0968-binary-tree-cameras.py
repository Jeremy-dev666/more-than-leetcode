# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 对于当前节点有三种状态：
        # 1.设置了摄像头，覆盖了自己
        # 2.不设置摄像头，但是被覆盖了
        # 3.不设置摄像头，并且没有被覆盖

        self.ans = 0
        NOT_COVERED, COVERED, HAS_CAMERA = 0, 1, 2

        def dfs(node):
            if not node:
                return COVERED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == NOT_COVERED or right == NOT_COVERED:
                self.ans += 1
                return HAS_CAMERA

            if left == HAS_CAMERA or right == HAS_CAMERA:
                return COVERED

            return NOT_COVERED

        # 后序遍历，根节点也需要检查一下最终状态
        if dfs(root) == NOT_COVERED:
            self.ans += 1
        return self.ans