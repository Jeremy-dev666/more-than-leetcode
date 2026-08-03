# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        
        def dfs(node):
            nonlocal ans
            if node is None:
                return []

            if not node.left and not node.right:
                return [1]

            left_list = dfs(node.left)
            right_list = dfs(node.right)

            for l in left_list:
                for r in right_list:
                    if l + r <= distance:
                        ans += 1

            cur = [d + 1 for d in left_list + right_list if d + 1 <= distance]
            return cur

        ans = 0
        dfs(root)
        return ans