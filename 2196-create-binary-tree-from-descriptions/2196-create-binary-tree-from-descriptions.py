# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for pa, ch, is_left in descriptions:
            if pa not in nodes:
                nodes[pa] = TreeNode(pa)
            if ch not in nodes:
                nodes[ch] = TreeNode(ch)

            if is_left:
                nodes[pa].left = nodes[ch]
            else:
                nodes[pa].right = nodes[ch]

            children.add(ch)

        for val, node in nodes.items():
            if val not in children:
                return node