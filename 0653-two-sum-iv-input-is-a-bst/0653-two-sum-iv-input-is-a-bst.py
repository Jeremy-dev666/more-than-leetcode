# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ans = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)

        dfs(root)
        l, r = 0, len(self.ans) - 1
        while l < r:
            if self.ans[l] + self.ans[r] == k:
                return True
            elif self.ans[l] + self.ans[r] < k:
                l += 1
            elif self.ans[l] + self.ans[r] > k:
                r -= 1
        return False
