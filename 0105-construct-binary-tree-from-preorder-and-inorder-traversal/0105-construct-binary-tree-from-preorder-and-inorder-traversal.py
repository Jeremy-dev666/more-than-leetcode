# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_mp = {val : idx for idx, val in enumerate(inorder)}

        def build(node_idx, in_start, in_end):
            if in_start > in_end:
                return None

            # 已知preorder里的node_idx，映射出inorder的索引
            in_idx = idx_mp[preorder[node_idx]]
            # in_idx左侧是左子树，右侧是右子树
            node = TreeNode(preorder[node_idx])

            # node_idx + 1 = 左子树段头节点，in_idx - 1 = 左子树段尾节点
            node.left = build(node_idx + 1, in_start, in_idx - 1)

            # in_idx - in_start = 左子树段长度
            # 左子树段长度 + node_idx + 1 = 右子树段头节点
            node.right = build(node_idx + (in_idx - in_start) + 1, in_idx + 1, in_end)

            return node

        return build(0, 0, len(inorder) - 1)
