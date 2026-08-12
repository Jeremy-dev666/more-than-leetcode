# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, arr):
            if node is None:
                return 

            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

        arr1, arr2 = [], []
        dfs(root1, arr1)
        dfs(root2, arr2)

        res = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        return res
