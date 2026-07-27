class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            new = ''.join(sorted(i))
            d[new].append(i)
        return list(d.values())
