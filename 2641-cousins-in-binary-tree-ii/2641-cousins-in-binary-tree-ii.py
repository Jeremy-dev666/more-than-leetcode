# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = deque([root])

        while q:
            nxt_level_q = deque()
            for node in q:
                if node.left:
                    nxt_level_q.append(node.left)
                if node.right:
                    nxt_level_q.append(node.right)

            nxt_level_sum = sum(node.val for node in nxt_level_q)

            for node in q:
                children_sum = 0
                if node.left:
                    children_sum += node.left.val
                if node.right:
                    children_sum += node.right.val

                if node.left:
                    node.left.val = nxt_level_sum - children_sum
                if node.right:
                    node.right.val = nxt_level_sum - children_sum

            q = nxt_level_q

        return root
