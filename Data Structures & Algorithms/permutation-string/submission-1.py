class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dic = {}
        for char in s1:
            dic[char] = dic.get(char, 0) + 1

        l = 0
        r = len(s1)

        while r <= len(s2):
            window = s2[l:r]
            window_dic = {}
            for char in window:
                window_dic[char] = window_dic.get(char, 0) + 1

            if window_dic == dic:
                return True

            l += 1
            r += 1
        return False