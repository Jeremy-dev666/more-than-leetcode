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

        # 找要删除的节点
        # 如果比当前节点小，那么没找到，往左子树递归继续找
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # 如果比当前节点大，那么没找到，往右子树递归继续找
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # 当root.val = key时，分情况讨论如何删除
        else:
            # 只有单子节点时直接顶替上来
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # 双子树（这里选择找右子树最小值来顶替）
            ptr = root.right
            while ptr.left:  # 往左走到底找到最小值
                ptr = ptr.left
            # 把值替换掉，并且同样地递归把这个最小值节点删除
            root.val = ptr.val
            root.right = self.deleteNode(root.right, ptr.val)

        return root
            

