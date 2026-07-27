class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0, len(matrix)-1
        while t <= b:
            mr = (t+b)//2
            if target < matrix[mr][0]:
                b = mr -1
            elif target > matrix[mr][-1]:
                t = mr + 1
            else:
                break
        if not(t <= b):
            return False
        l,r = 0,len(matrix[0])-1
        while l <= r:
            m = (l+r)//2
            if target < matrix[mr][m]:
                r = m-1
            elif target > matrix[mr][m]:
                l = m+1
            else:
                return True
        return False
