from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []
        self.backtrack(0, 0, [])
        return self.ans

    def backtrack(self, left: int, right: int, path: List[str]) -> None:
        if self.n * 2 == len(path):
            self.ans.append("".join(path))
            return
        
        if left < self.n:
            path.append("(")
            self.backtrack(left + 1, right, path)
            path.pop()

        if right < left:
            path.append(")")
            self.backtrack(left, right + 1, path)
            path.pop()      