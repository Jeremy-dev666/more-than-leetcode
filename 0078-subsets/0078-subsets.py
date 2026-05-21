class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans: List[List[int]] = []
        self.n = len(nums)
        self.nums = nums
        self.backtrack([], 0)
        return self.ans

    def backtrack(self, path: List[int], index: int) -> None:
        self.ans.append(list(path))

        for i in range(index, self.n):
            path.append(self.nums[i])
            self.backtrack(path, i + 1)
            path.pop()

    
