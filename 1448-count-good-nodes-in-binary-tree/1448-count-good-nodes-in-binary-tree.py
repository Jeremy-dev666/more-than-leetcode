class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, mx):
            nonlocal ans
            if node is None:
                return
            if node.val >= mx:
                ans += 1
                mx = max(mx, node.val)
            dfs(node.left, mx)
            dfs(node.right, mx)

        dfs(root, -float('inf'))
        return ans