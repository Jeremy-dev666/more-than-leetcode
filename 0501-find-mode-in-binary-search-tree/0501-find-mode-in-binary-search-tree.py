# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.cur_freq = self.max_freq = 0

        def dfs(node):
            nonlocal ans
            if node is None:
                return
            
            dfs(node.left)

            # 1.计算当前节点的频率
            if self.prev is not None and node.val == self.prev:
                self.cur_freq += 1
            else:
                self.cur_freq = 1
            # 2. 和最大值分情况比较
            if self.cur_freq > self.max_freq:
                self.max_freq = self.cur_freq
                ans = [node.val]  # 有新的最大频率，列表初始化重建
            elif self.cur_freq == self.max_freq:
                ans.append(node.val)
            
            self.prev = node.val
            dfs(node.right)

        ans = []
        dfs(root)
        return ans