class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and nums[i-1]==val:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]+val < 0:
                    l+=1
                elif nums[l]+nums[r]+val > 0:
                    r-=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res