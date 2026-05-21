class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(index: int, sum: int, path: List[int]) -> None:
            """
            index 决定要走哪个分岔路口
            i     决定下一步从哪开始
            """
            if sum == target:
                ans.append(list(path))
                return
            if sum > target:
                return
            
            for i in range(index, n):
                num = candidates[i]
                sum += num
                path.append(num)
                backtrack(i, sum, path)
                sum -= num
                path.pop()

        backtrack(0, 0, [])
        return ans