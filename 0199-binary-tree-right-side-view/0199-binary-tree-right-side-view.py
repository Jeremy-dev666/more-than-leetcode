# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        
        dq = deque([root])
        while dq:
            sz = len(dq)
            for i in range(sz):
                node = dq.popleft()
                if i == sz - 1:
                    ans.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return ans
                