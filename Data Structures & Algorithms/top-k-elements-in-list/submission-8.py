class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        
        fin = [[] for _ in range(len(nums)+1)]
        for i,n in count.items():
            fin[n].append(i)
        res = []
        for i in range(len(fin)-1,0,-1):
            for num in fin[i]:
                res.append(num)
                if len(res)==k:
                    return res