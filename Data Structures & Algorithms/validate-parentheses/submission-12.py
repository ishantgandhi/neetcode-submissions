class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char not in dic:
                stack.append(char)
            else:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()
        return not stack