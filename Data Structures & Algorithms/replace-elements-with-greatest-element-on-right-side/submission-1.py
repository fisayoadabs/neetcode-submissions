class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                result.append(-1)
                break
            maxVal = 0
            j = i + 1
            while j < len(arr):
                maxVal = max(arr[j], maxVal)
                j+=1
            result.append(maxVal)
        return result
        