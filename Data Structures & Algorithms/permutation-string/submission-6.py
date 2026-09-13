class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1

        window_count = {}
        for char in s2[:len(s1)]:
            window_count[char] = window_count.get(char, 0) + 1
        if window_count == count:
                return True
        start = 0
        end = len(s1)

        while end < len(s2):            
            if window_count == count:
                return True
            window_count[s2[start]] -= 1
            if window_count[s2[start]] == 0:
                del window_count[s2[start]]
            start += 1
            window_count[s2[end]] = window_count.get(s2[end], 0) + 1
            end += 1
            if window_count == count:
                return True
        return False


        