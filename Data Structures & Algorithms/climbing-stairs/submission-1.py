class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i,n,cache):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            else:
                cache[i] = climb(i+1,n,cache)+climb(i+2,n,cache)
                return cache[i]
        return climb(0,n,{})
