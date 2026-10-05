class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap ={}
        nest = set()
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in nest:
                    return False

                hashmap[s[i]] = t[i]
                nest.add(t[i])
        return True
