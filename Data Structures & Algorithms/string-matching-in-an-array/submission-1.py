class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        length = len(words)
        result = set()
        for i in range(length):
            for j in range(length):
                if i!=j and words[i] in words[j]:
                    result.add(words[i])
        return list(result)

