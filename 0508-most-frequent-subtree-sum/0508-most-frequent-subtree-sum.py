# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # 收集子树和
        def dfs(node):
            if node is None:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)
            ans.append(total)
            return total

        dfs(root)

        # 统计频次并返回最高的
        cnt = Counter(ans)
        max_f = max(cnt.values())  # 取到频次最高的数值
        return [tree_sum  for tree_sum , freq in cnt.items() if freq == max_f]