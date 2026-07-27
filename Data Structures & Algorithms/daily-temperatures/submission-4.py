class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                temp = stack.pop()
                ans[temp] = i - temp
            stack.append(i)
        return ans