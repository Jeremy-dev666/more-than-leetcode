# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # floor and ceiling val
        # 中序遍历搜集结果
        self.arr = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
            
        dfs(root)

        ans = []
        for q in queries:
            # bisect.bisect_left: 在一个已排序的数组中的找到第一个比查询元素大于等于的数索引
            idx = bisect.bisect_left(self.arr, q)
            # idx 是第一个 >= q 的位置
            if idx < len(self.arr) and self.arr[idx] == q:
                ans.append([q, q])
            else:
                mn = self.arr[idx - 1] if idx > 0 else -1
                mx = self.arr[idx] if idx < len(self.arr) else -1
                ans.append([mn, mx])

        return ans