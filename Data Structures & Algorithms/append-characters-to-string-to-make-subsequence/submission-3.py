class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        c_index = 0
        for i in s:
            if c_index<len(t) and t[c_index] == i:
                c_index += 1
        return len(t) - c_index
             


        