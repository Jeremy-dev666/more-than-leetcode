# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # 路径拼接函数
        def dfs(node, target, path):
            if node is None:
                return False
            if node.val == target:
                return True
            
            path.append('L')  # 往左找目标节点
            if dfs(node.left, target, path):
                return True
            path.pop()        # 恢复现场

            path.append('R')  # 往右找目标节点
            if dfs(node.right, target, path):
                return True
            path.pop()        # 恢复现场

            return False 

        start_path, dest_path = [], []
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)

        # 去掉路径公共前缀
        ptr = 0
        while ptr < len(start_path) and ptr < len(dest_path) and start_path[ptr] == dest_path[ptr]:
            ptr += 1

        ups = 'U' * (len(start_path) - ptr)
        downs = ''.join(dest_path[ptr:])
        return ups + downs
            