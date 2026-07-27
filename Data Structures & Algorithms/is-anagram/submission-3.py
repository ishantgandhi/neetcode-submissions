class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(string: str, dic: dict) -> dict:
            for char in string:
                if char in dic:
                    dic[char]+=1
                else:
                    dic[char]=0
            return dic
        dic1 = {}
        dic2 = {}
        dic1 = helper(s,dic1)
        dic2 = helper(t,dic2)
        if dic1 == dic2:
            return True
        else:
            return False
        
        