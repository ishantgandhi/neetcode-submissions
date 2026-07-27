class Solution:

    def encode(self, strs: List[str]) -> str:
        joint = ""
        for word in strs:
            joint+= str(len(word))+'/'+ word
        return joint

    def decode(self, s: str) -> List[str]:
        broken = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '/':
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            word = s[i:j]
            broken.append(word)
            i = j
        return broken
