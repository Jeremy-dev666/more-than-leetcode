class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for x in arr1:
            target = x - d

            l, r = 0, len(arr2)
            while l < r:
                mid = (l + r) // 2
                if arr2[mid] < target:
                    l = mid + 1
                else:
                    r = mid

            i = l

            if i == len(arr2) or arr2[i] > x + d:
                ans += 1

        return ans