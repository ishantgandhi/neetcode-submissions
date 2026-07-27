class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        dist = []
        res = []
        for point in points:
            d = sqrt((point[0]**2)+(point[1]**2))
            dist.append([d,[point[0],point[1]]])
        heapq.heapify(dist)
        while k > 0:
            r = heapq.heappop(dist)
            res.append(r[1])
            k-=1
        return res