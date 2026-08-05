# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        buckets = []

        def dfs(node):
            # 让真正的叶子节点作为第0层（即索引0）
            if not node:
                return -1
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            height = max(leftHeight, rightHeight) + 1

            if height == len(buckets):
                buckets.append([])
            buckets[height].append(node.val)
            
            return height

        dfs(root)
        return buckets