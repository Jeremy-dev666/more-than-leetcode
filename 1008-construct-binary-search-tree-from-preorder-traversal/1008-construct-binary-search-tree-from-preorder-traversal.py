# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        n = len(preorder)

        def build(bound):
            if self.idx == n or preorder[self.idx] > bound:
                return None
                
            cur_val = preorder[self.idx]
            self.idx += 1
            node = TreeNode(cur_val)

            node.left = build(cur_val)
            node.right = build(bound)
            return node

        return build(float('inf'))