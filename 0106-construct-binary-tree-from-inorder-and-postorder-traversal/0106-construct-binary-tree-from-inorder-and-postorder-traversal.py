# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx_mp = {val : idx for idx, val in enumerate(inorder)}
        self.postIdx = len(postorder) - 1

        def build(start, end):
            if start > end:
                return None

            root_val = postorder[self.postIdx]
            root = TreeNode(root_val)
            self.postIdx -= 1
            root.right = build(self.idx_mp[root_val] + 1, end)
            root.left = build(start, self.idx_mp[root_val] - 1)
            return root

        return build(0, len(inorder) - 1)
        
