# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st = []
        if root is not None:
            st.append((1, root))
        
        ans = 0
        while st:
            cur_depth, root = st.pop()
            if root:
                ans = max(ans, cur_depth)
                st.append((cur_depth + 1, root.left))
                st.append((cur_depth + 1, root.right))

        return ans

        