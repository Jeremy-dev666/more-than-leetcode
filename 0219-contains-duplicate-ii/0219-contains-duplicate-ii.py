from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = defaultdict(int)
        for i in range(n):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        return False
