class Solution:

    def encode(self, strs: List[str]) -> str:
        joint = ""
        for s in strs:
            joint += str(len(s)) + "/" + s
        return joint

    def decode(self, s: str) -> List[str]:
        i = 0
        broken = []
        while i < len(s):
            j = i
            while s[j] != "/":
                j += 1
            l = int(s[i:j])
            i = j + 1
            broken.append(s[i : i + l])
            i = i + l
        return broken