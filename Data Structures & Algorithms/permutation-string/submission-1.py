class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1
        
        start = 0
        end = len(s1)

        while end <= len(s2):
            window = s2[start:end]
            window_count = {}
            for char in window:
                window_count[char] = window_count.get(char, 0) + 1
            if window_count == count:
                return True
            start += 1
            end += 1
        return False


        