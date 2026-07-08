class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(path, start):
            nonlocal ans
            if sum(path) == target:
                ans.append(list(path))
            elif sum(path) > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i)
                path.pop()

        backtrack([], 0)
        return ans