# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, freq):
            if node is None:
                return
            freq[node.val] += 1
            dfs(node.left,freq)
            dfs(node.right, freq)


        freq = defaultdict(int)
        dfs(root, freq)
        max_val = max(freq.values())

        ans = []
        for key in freq:
            if freq[key] == max_val:
                ans.append(key)

        return ans
