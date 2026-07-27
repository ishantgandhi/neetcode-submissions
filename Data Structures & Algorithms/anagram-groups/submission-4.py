class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for stri in strs:
            base = "".join(sorted(stri))
            d[base].append(stri)
        return list(d.values())
    