# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def build(node):
            if node is None:
                return TreeNode(val)

            if node.val < val:
                new_node = TreeNode(val, left=node)
                return new_node

            # 因为val节点是添加在原数组最后，所以遍历的时候只往右走
            node.right = build(node.right)
            return node

        return build(root)
            