# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.ans = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.ans.append(node)
            dfs(node.right)

        dfs(root)

        for i in range(len(self.ans)):
            if i < (len(self.ans) - 1) and self.ans[i].val == p.val:
                return self.ans[i + 1]
        return None