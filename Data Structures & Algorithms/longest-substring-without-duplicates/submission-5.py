class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        right = 1
        result = 0
        while right < len(s):
            if s[right] in s[left:right]:
                result = max(result, (right - left))
                left += 1
            else:
                result = max(result, (right - left)+1)
                right+=1
        return result

        