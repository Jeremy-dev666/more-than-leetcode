# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return (0, 0)  # (cnt_nodes, sum)
            
            left_cnt, left_sum = dfs(node.left)
            right_cnt, right_sum = dfs(node.right)
            total_sum = node.val + left_sum + right_sum
            total_cnt = left_cnt + right_cnt + 1
            avg = total_sum / total_cnt
            ans = max(ans, avg)

            return (total_cnt, total_sum)

        ans = 0
        dfs(root)
        return ans