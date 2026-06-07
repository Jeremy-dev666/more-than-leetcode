class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)
        for i in range (n):
            t = target - nums[i]
            if t in mp:
                return [i, mp[t]]
            mp[nums[i]] = i
        return []