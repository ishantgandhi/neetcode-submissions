class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        curr = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                curr = max(curr,prices[r]-prices[l])
            r+=1
        return curr
            