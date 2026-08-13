# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. 先取出有序数组
        self.arr = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)

        # 2. 重新构造平衡搜索树
        def build(arr, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            new_node = TreeNode(arr[mid])
            new_node.left = build(arr, start, mid - 1)
            new_node.right = build(arr, mid + 1, end)

            return new_node

        return build(self.arr, 0, len(self.arr) - 1)