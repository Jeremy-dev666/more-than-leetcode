class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        rows = [[] for _ in range(numRows)]

        i, flag = 0, -1
        for c in s:
            rows[i].append(c)
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        
        return "".join("".join(row) for row in rows)