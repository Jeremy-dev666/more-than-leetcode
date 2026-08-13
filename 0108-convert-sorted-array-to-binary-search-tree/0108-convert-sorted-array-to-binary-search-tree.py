# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(arr: List[int], start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None

            mid = (start + end) // 2
            node = TreeNode(arr[mid])
            node.left = build(arr, start, mid - 1)
            node.right = build(arr, mid + 1, end)

            return node

        return build(nums, 0, len(nums) - 1)


    