class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            if i == "+":
                if len(result) >= 2:
                    result.append(result[-2] + result[-1])
            elif i == "C":
                result.pop()
            elif i == "D":
                result.append(2*result[-1])
            else:
                result.append(int(i))
        
        return sum(result)
        