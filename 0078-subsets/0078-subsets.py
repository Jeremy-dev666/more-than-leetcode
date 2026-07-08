class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, subset):
            result.append(list(subset))
            for cur in range(start, len(nums)):
                subset.append(nums[cur])
                backtrack(cur + 1, subset)
                subset.pop()
        backtrack(0, [])
        return result