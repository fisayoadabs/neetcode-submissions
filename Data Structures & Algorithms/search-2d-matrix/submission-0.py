class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low = 0
            high = len(matrix[i]) - 1
            while(low<=high):
                middle = (low + high) // 2
                value = matrix[i][middle]
                if(value < target):
                    low = middle + 1
                elif(value > target):
                    high = middle - 1
                else:
                    return True
        return False

        