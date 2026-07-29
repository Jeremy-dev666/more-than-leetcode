# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, idx):
            if node is None:
                return False

            if node.val != arr[idx]:
                return False

            if idx == len(arr) - 1:
                if not node.left and not node.right:
                    return True
                else:
                    return False

            idx += 1
            return dfs(node.left, idx) or dfs(node.right, idx)

        return dfs(root, 0)
        