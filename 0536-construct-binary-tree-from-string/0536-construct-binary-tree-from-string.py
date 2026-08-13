# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if len(s) == 0:
            return None

        ptr = 0
        def parse_number():
            nonlocal ptr
            start = ptr
            if s[ptr] == '-':
                ptr += 1
            while ptr < len(s) and s[ptr].isdigit():
                ptr += 1
            return int(s[start:ptr])

        def parse_tree():
            nonlocal ptr
            val = parse_number()
            node = TreeNode(val)

            if ptr < len(s) and s[ptr] == '(':
                ptr += 1
                node.left = parse_tree()
                ptr += 1

            if ptr < len(s) and s[ptr] == '(':
                ptr += 1
                node.right = parse_tree()
                ptr += 1

            return node

        return parse_tree()
        