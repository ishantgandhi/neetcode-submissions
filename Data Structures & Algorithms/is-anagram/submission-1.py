class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for letter in s:
            if letter not in dic1:
                dic1[letter] = 1
            else:
                dic1[letter] += 1

        for letter in t:
            if letter not in dic2:
                dic2[letter] = 1
            else:
                dic2[letter] += 1
        return dic1 == dic2
        