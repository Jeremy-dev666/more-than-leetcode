class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. 找山顶
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        # 2. 左边升序二分
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            cur = mountainArr.get(mid)

            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1

        # 3. 右边降序二分
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            cur = mountainArr.get(mid)

            if cur == target:
                return mid
            elif cur > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1