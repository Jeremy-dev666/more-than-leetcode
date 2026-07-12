class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = [''] * (2 * n)
        ans  = []
        def backtrack(l, r):
            if r == n:
                ans.append(''.join(path))
                return

            if l < n:
                path[l+ r] = '('
                backtrack(l + 1, r)
            if r < l:
                path[l + r] = ')'
                backtrack(l, r + 1)

        backtrack(0, 0)
        return ans