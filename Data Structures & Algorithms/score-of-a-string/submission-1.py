class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        i = 0
        while i+1 < len(s):
            total += abs(ord(s[i]) - ord(s[i+1]))
            i+=1
        return total
        