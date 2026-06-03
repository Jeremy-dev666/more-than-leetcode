class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def find(startTime1, duration1, startTime2, duration2):
            n = len(startTime1)
            m = len(startTime2)
            first_finish = inf
            for i in range (n):
                first_finish = min(first_finish, startTime1[i] + duration1[i])
            later_finish = inf
            for j in range (m):
                later_finish = min(later_finish, max(first_finish, startTime2[j]) + duration2[j])
            return later_finish

        land_water = find(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = find(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)