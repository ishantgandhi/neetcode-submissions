class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            new = ''.join(sorted(word))
            dic[new].append(word)
        return list(dic.values()) 