# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        def dfs(node, counter):
            if not node:
                return

            if node.val != '+':
                counter[node.val] += 1
                return

            dfs(node.left, counter)
            dfs(node.right, counter)

        count1 = collections.Counter()
        count2 = collections.Counter()
        dfs(root1, count1)
        dfs(root2, count2)

        return count1 == count2

        