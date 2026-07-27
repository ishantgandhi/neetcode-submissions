class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        res = 0
        while l<r:
            curr = min(heights[l],heights[r]) * (r-l)
            res = max(res,curr)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1
        return res
