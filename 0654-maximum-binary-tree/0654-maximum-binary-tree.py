# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        st = []
        for num in nums:
            new_node = TreeNode(num)
            last_smaller = None

            # 维护单调递减栈
            # 弹出的最后一个栈顶元素就是比当前节点值小的最大元素
            while st and st[-1].val < num:
                last_smaller = st.pop()
            new_node.left = last_smaller

            # 如果栈内还有元素，说明栈顶比当前节点值大，当前节点挂在栈顶节点右子树
            if st:
                st[-1].right = new_node

            st.append(new_node)

        return st[0] if st else None