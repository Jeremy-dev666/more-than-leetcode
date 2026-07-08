class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(path, start, remain):
            if remain == 0:
                ans.append(list(path))
                return

            for i in range(start, len(candidates)):
                # 剪枝
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(path, i, remain - candidates[i])
                path.pop()

        backtrack([], 0, target)
        return ans