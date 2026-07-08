class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)

        def backtrack(path, start, remain):
            if remain == 0:
                ans.append(list(path))
                return

            for i in range(start, n):
                # 同一层中，跳过重复的候选值（避免生成重复组合）
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtrack(path, i + 1, remain - candidates[i])
                path.pop()

        backtrack([], 0, target)
        return ans