class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        current_index = 0
        result = 0
        for i in range(len(t)):
            n_index = s[current_index:].find(t[i])
            if n_index != -1:
                current_index += n_index + 1
            else:
                 result = len(t[i:])
                 break
        return result
             


        