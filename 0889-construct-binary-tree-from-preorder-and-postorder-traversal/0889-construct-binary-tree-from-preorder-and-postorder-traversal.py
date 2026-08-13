# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_mp = {val: idx for idx, val in enumerate(postorder)}

        def build(pre_start, pre_end, post_start):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])
            # 叶子节点
            if pre_start == pre_end:
                return root

            left_root_val = preorder[pre_start + 1]
            left_size = idx_mp[left_root_val] - post_start + 1

            root.left = build(pre_start + 1, pre_start + left_size, post_start)
            root.right = build(pre_start + left_size + 1, pre_end, post_start + left_size)
            return root

        return build(0, len(preorder) - 1, 0)