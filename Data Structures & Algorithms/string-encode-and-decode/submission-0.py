class Solution:

    def encode(self, strs: List[str]) -> str:
        encStr = ""
        for word in strs:
            encStr+=str(len(word))+'/'+word
        return encStr

    def decode(self, s: str) -> List[str]:
        decList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '/':
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            decList.append(s[i:j])
            i=j
        return decList

