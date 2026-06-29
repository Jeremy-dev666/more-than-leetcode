from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = self.tm[key]
        if val:
            if val[-1][1] <= timestamp:
                return val[-1][0]

            l, r = 0, len(val)
            while l < r:
                mid = (l + r) // 2
                if val[mid][1] > timestamp:
                    r = mid
                else:
                    l = mid + 1
            if l - 1 < len(val) and val[l - 1][1] <= timestamp:
                return val[l - 1][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)