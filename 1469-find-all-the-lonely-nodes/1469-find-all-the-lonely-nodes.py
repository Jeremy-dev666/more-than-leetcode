# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        # 有爸妈但是没有兄弟 -> 查小孩（有且只有一个）
        def dfs(node):
            nonlocal ans
            if node is None:
                return

            if node.left and not node.right:
                ans.append(node.left.val)
            if node.right and not node.left:
                ans.append(node.right.val)

            dfs(node.left)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans
