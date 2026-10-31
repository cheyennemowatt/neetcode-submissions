class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #loop through every row
        for r in range (len(matrix)):
            #loop through every column
            #we get length of column using length of first column
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
        
        
        
        
