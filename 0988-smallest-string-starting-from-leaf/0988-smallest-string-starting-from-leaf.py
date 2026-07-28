# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, path):
            nonlocal ans
            if node is None:
                return

            path.append(chr(node.val + ord('a')))

            if node.left is None and node.right is None:
                tmp = ''.join(reversed(path))
                if ans is None or tmp < ans:
                    ans = tmp

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        ans = None
        dfs(root, [])
        return ans