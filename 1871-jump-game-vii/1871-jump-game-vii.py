class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        n = len(s)
        reach = [False] * n
        reach[0] = True
        j = 1
        for i, c in enumerate(s):
            if c == "0" and reach[i]:
                farthest = min(i + maxJump, n - 1)
                j = max(j, i + minJump)
                while j <= farthest:
                    reach[j] = True
                    j += 1
                if j == n:
                    break

        return reach[-1]