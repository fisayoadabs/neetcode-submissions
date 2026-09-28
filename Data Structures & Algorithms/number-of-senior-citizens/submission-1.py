class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for det in details:
            age = det[11:13]
            if int(age) > 60:
                result+=1
        return result
        