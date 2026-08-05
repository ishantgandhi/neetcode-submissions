class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]
        def dfs(i,numz,cache):
            if i >= len(numz):
                return 0
            if i in cache:
                return cache[i]
            else:
                cache[i] = max(dfs(i+1,numz,cache),numz[i]+dfs(i+2,numz,cache))
                return cache[i]
        return max(dfs(0,nums1,{}),dfs(0,nums2,{}))