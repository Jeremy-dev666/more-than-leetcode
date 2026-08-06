# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.mp = defaultdict(int)
        self.mp[0] = 1

        def dfs(node, total):
            nonlocal ans
            if node is None:
                return

            total += node.val
            target = total - targetSum
            ans += self.mp[target]
            self.mp[total] += 1

            dfs(node.left, total)
            dfs(node.right, total)

            self.mp[total] -= 1

        ans = 0
        dfs(root, 0)
        return ans