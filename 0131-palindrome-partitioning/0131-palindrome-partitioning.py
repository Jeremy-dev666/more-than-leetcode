class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        # 子串s[start:i + 1]
        def dfs(path, start):
            if start == n:
                ans.append(path.copy())
                return
            
            # 枚举分割的位置
            for i in range(start, n):
                t = s[start:i+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(path, i+1)
                    path.pop()

        dfs([], 0)
        return ans
