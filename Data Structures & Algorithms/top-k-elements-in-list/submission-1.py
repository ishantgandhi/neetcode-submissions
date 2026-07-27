class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        values = []
        for val in dic.values():
            values.append(val)
        values.sort(reverse = True)
        keys = []
        l = 0
        while l < k:
            for key, value in dic.items():
                if value == values[l] :
                    if key not in keys:
                        keys.append(key)
            l+=1
        return keys