class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        
        # 子串s[start:i + 1]
        def dfs(path, start, i):
            if i == n:
                ans.append(path.copy())
                return
            
            # 不分割，继续递归
            if i < n - 1:
                dfs(path, start, i + 1)

            # 分割
            # 验证是否是回文
            t = s[start:i+1]
            if t == t[::-1]:
                path.append(t)
                dfs(path, i+1, i+1)
                path.pop()

        dfs([], 0, 0)
        return ans
