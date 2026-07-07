import heapq
class KthLargest:
    # [k, arr[]]
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = nums
        heapq.heapify(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        while len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)