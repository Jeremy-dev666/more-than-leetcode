# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        st, ans = [], []
        node = root

        while node or st:
            # 中序，一路向左到底
            while node:
                st.append(node)
                node = node.left

            # 处理当前节点
            node = st.pop()
            ans.append(node.val)

            # 转向右
            node = node.right

        return ans
            