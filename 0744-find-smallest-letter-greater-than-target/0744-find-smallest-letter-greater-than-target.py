class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            c = letters[mid]
            if c <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l] if l != n else letters[0]