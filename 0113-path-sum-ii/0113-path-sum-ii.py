# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans, path = [], []
        def dfs(node, target):
            if not node:
                return

            target -= node.val
            path.append(node.val)
            if target == 0 and not node.left and not node.right:
                ans.append(list(path))

            dfs(node.left, target)
            dfs(node.right, target)

            path.pop()

        dfs(root, targetSum)
        return ans