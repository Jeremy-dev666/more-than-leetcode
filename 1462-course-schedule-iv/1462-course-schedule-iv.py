class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False] * numCourses for _ in range(numCourses)]
        for fr, to in prerequisites:
            dp[fr][to] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if dp[i][k] and dp[k][j]:
                        dp[i][j] = True

        ans = []
        for i, j in queries:
            ans.append(dp[i][j])
        return ans