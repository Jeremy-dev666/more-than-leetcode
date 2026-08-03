# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sub_sums = []  # 记录每棵子树的和

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sub_sums.append(s)
            return s

        total = dfs(root)
        sub_sums.pop()  # 弹掉最后一个：它是整棵树的和，不能作为"被切掉的子树"

        return total % 2 == 0 and total // 2 in sub_sums