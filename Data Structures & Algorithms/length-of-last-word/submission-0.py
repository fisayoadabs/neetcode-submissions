class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        remove_space = s.split()
        return len(remove_space[-1])
        