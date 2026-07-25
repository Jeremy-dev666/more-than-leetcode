class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        can_reaches = [False] * n
        can_reaches[0] = True

        j = 1
        for i, ch in enumerate(s):
            if ch == '0' and can_reaches[i]:
                # 注意 j 只会增大，不会减小，所以总体时间复杂度是 O(n)
                mx = min(i + maxJump, n - 1)
                j = max(j, i + minJump)
                while j <= mx:                    
                    can_reaches[j] = True  # 可以跳到 j
                    j += 1
                if j == n:
                    break

        return s[-1] == '0' and can_reaches[-1]