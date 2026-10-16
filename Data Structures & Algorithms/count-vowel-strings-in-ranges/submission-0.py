class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for i, j in queries:
            count = 0
            for k in range(i,j+1):
                if words[k][0].lower() in "aeiou" and words[k][-1].lower() in "aeiou":
                    count+=1
            result.append(count)
        return result
        