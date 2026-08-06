# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, total):
            if not node:
                return None
            total += node.val

            # 只有到达叶子节点时才决定是否删除
            if not node.left and not node.right:
                return node if total >= limit else None

            node.left = dfs(node.left, total)
            node.right = dfs(node.right, total)

            # 如果左右子树都是不充足的，那么当前节点也是不充足的，返回None
            return node if (node.left or node.right) else None

        return dfs(root, 0)