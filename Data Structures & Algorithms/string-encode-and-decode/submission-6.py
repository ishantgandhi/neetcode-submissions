class Solution:

    def encode(self, strs: List[str]) -> str:
        estr = ""
        for s in strs:
            estr += str(len(s))+"?"+s
        return estr
            


    def decode(self, s: str) -> List[str]:
        dstr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "?":
                j+=1
            l = int(s[i:j])
            i = j+1
            dstr.append(s[i:i+l])
            i = i+l
        return dstr

