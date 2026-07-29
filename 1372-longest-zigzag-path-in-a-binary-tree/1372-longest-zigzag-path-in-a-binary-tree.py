# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, prev_dir, cur_len):  # dir: left true  right false
            nonlocal ans
            if node is None:
                return

            ans = max(ans, cur_len)

            # 向左子树走，传进来的方向应该是向右cur_len + 1
            dfs(node.left, True, cur_len + 1 if not prev_dir else 1)
            # 向右子树走，传进来的方向应该是向左cur_len + 1
            dfs(node.right, False, cur_len + 1 if prev_dir else 1)

        ans = 0
        dfs(root, True, 0)
        return ans


            

            