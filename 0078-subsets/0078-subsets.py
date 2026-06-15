class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def bt(path, idx):
            self.ans.append(list(path))
            for i in range(idx, len(nums)):
                path.append(nums[i])
                bt(path, i + 1)
                path.pop()

        bt([], 0)
        return self.ans
