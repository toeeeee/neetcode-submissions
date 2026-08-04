class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i,j = 0,m*n-1
        mid = j // 2
        while i <= j: 
            row = mid // n
            col = mid % n
            item = matrix[row][col]
            if item == target:
                return True
            elif item < target:
                i = mid+1
            elif item > target:
                j = mid-1
            mid = (i+j)//2 

        return False

