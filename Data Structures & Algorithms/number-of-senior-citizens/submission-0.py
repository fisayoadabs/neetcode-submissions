class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for det in details:
            phone = det[:10]
            gender = det[10]
            age = det[11:13]
            seat = det[13:]
            if int(age) > 60:
                result+=1
        return result
        