# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # 题目和层有关首先考虑BFS

        # 边界特殊情况
        if depth == 1:
            return TreeNode(val, root, None)
        
        q = deque([root])
        D = 1
        while q:
            D += 1
            sz = len(q)
            
            for _ in range(sz):
                cur = q.popleft()
                if D == depth:
                    left, right = cur.left, cur.right
                    cur.left = TreeNode(val, left, None)
                    cur.right = TreeNode(val, None, right)
                else:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)

            if D == depth:
                break

        return root