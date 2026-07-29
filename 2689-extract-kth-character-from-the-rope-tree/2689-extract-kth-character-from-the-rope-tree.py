# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        def dfs(node, k):
            # 叶子节点直接返回对应字符
            if node.len == 0:
                return node.val[k - 1]

            # 计算左子树长度，就能知道右子树长度
            left_len = 0
            if node.left:
                # 判断左子树是叶子节点或是内部节点
                if node.left.len > 0:
                    left_len = node.left.len
                else:  # node.left.len = 0
                    left_len = len(node.left.val)

            if k <= left_len:
                return dfs(node.left, k)
            else:
                return dfs(node.right, k - left_len)
        
        return dfs(root, k)