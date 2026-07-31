class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        parts = []

        def dfs(node):
            if node is None:
                return
            parts.append(str(node.val))
            if node.left or node.right:
                parts.append('(')
                dfs(node.left)
                parts.append(')')
            if node.right:
                parts.append('(')
                dfs(node.right)
                parts.append(')')

        dfs(root)
        return ''.join(parts)