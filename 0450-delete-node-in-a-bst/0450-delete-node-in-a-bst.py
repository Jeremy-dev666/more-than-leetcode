# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # 1. 利用bst去找到目标节点匹配当前遍历到的节点
        # 1.1 没找到，小，去左子树继续找，删除后会返回节点重新挂载
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # 1.2 没找到，大，去右子树继续找，删除后会返回节点重新挂载
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # 1.3 和当前节点匹配，分情况讨论：
        else:
            # 1.3.1 当前节点只有左或右孩子或者为叶子节点，直接返回另一方
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # 1.3.2 当前节点左右孩子都有，那么有两种选择方案
            # 找左子树最大 或者 找右子树最小
            # 此题解选择找右子树最小（往右子树一路向左走到底）
            ptr = root.right
            while ptr.left:
                ptr = ptr.left
            # 找到右子树最小值替换到当前节点值
            root.val = ptr.val
            # 然后问题替换成从当前右子树开始继续递归删除刚刚找到的最小值节点
            root.right = self.deleteNode(root.right, ptr.val)
        
        return root




