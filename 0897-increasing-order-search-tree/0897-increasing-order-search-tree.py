# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.ans.append(node)
            dfs(node.right)

        dfs(root)

        for i in range(len(self.ans)):
            self.ans[i].left = None
            if i + 1 < len(self.ans):
                self.ans[i].right = self.ans[i + 1]
            else:
                self.ans[i].right = None

        return self.ans[0] if self.ans else None