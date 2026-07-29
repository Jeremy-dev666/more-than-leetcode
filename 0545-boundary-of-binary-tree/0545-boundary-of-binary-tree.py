# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        def isLeaf(node):
            return not node.left and not node.right
        
        # 收集左边界（不含叶子节点），自顶向下
        def leftBoundary(node):
            res = []
            while node and not isLeaf(node):
                res.append(node.val)
                node = node.left if node.left else node.right
            return res
        
        # 收集右边界（不含叶子节点），自顶向下先收集，最后需要反转
        def rightBoundary(node):
            res = []
            while node and not isLeaf(node):
                res.append(node.val)
                node = node.right if node.right else node.left
            return res[::-1]
        
        # 收集所有叶子节点，从左到右（不含根节点本身）
        def leaves(node):
            if not node:
                return []
            if isLeaf(node):
                return [node.val]
            return leaves(node.left) + leaves(node.right)
        
        # 如果根节点本身就是叶子，直接返回根节点
        if isLeaf(root):
            return [root.val]
        
        result = [root.val]
        result += leftBoundary(root.left)
        result += leaves(root)
        result += rightBoundary(root.right)
        
        return result