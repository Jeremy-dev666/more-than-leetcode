# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        qo = deque([original])
        qc = deque([cloned])
        while qo:
            cur = qo.popleft()
            c = qc.popleft()
            if cur is target:
                return c

            if cur.left:
                qo.append(cur.left)
                qc.append(c.left)
            if cur.right:
                qo.append(cur.right)
                qc.append(c.right)

        

