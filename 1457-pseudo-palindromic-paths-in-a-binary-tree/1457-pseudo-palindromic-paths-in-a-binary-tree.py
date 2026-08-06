# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, counter):
            nonlocal ans
            if node is None:
                return
            
            counter[node.val] += 1

            if node.left is None and node.right is None:
                odd_count = sum(1 for val in counter.values() if val % 2 == 1)
                if odd_count <= 1:
                    ans += 1

            dfs(node.left, counter)
            dfs(node.right, counter)

            counter[node.val] -= 1

        ans = 0
        dfs(root, Counter())
        return ans