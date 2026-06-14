from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        n = len(nums)
        sum = ans = 0
        
        for i in range(n):
            sum += nums[i]
            target = sum - k
            if target in mp:
                ans += mp[target]
            mp[sum] += 1
        return ans
