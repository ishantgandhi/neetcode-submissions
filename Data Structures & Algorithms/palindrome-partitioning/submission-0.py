class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(word):
            l = 0
            r = len(word)-1
            while l<=r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        
        res = []
        def dfs(i,sub):
            if i == len(s):
                res.append(sub.copy())
                return
            for j in range(i+1,len(s)+1):
                pre = s[i:j]
                if check(pre):
                    sub.append(pre)
                    dfs(j,sub)
                    sub.pop()
        dfs(0, [])
        return res
