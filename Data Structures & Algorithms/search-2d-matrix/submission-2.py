class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1
        while(low<=high):
            middle = (low + high) // 2
            row = middle // cols
            col = middle % cols
            value = matrix[row][col]
            if(value < target):
                low = middle + 1
            elif(value > target):
                high = middle - 1
            else:
                return True
        return False

        