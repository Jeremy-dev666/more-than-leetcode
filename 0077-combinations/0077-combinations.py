class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(path, start):
            if len(path) == k:
                ans.append(list(path))
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 1)
        return ans
