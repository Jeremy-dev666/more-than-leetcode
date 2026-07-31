class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, went_left, length):
            nonlocal ans
            if node is None:
                return
            ans = max(ans, length)
            if went_left:
                dfs(node.left, True, 1)
                dfs(node.right, False, length + 1)
            else:
                dfs(node.left, True, length + 1)
                dfs(node.right, False, 1)

        dfs(root, True, 0)
        return ans