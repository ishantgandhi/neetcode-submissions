class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0,len(matrix)-1
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot-=1
            elif target > matrix[row][-1]:
                top+=1
            else:
                break
        
        if not(top <= bot):
            return False
        
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            if target < matrix[row][mid]:
                r-=1
            elif target > matrix[row][mid]:
                l+=1
            else:
                return True
        return False
        
            