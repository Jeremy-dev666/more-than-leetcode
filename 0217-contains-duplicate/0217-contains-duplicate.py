class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for k in nums:
            if k in visited:
                return True
            else:
                visited.add(k)
        return False