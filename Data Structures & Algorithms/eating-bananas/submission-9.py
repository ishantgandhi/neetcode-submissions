class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <=r:
            k = (l+r)//2
            hr = 0
            for num in piles:
                hr += math.ceil(num/k)
            if hr > h:
                l = k+1
            else:
                res = k
                r = k-1
        return res