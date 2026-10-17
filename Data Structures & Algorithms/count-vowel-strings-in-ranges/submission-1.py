class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        cc=[]
        result = []

        for k in range(len(words)):
            if words[k][0].lower() in "aeiou" and words[k][-1].lower() in "aeiou":
                cc.append(1)
            else:
                cc.append(0)
        for i, j in queries:
            count = sum(cc[i:j+1])
            result.append(count)
        return result
        