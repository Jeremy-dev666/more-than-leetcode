# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        st, ans = [root], []

        while st:
            cur = st.pop()
            ans.append(cur.val)
            
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)

        return ans[::-1]
