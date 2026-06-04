class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in range(len(strs)):
            check = "".join(sorted(strs[i]))
            if check in hashmap:
                hashmap[check].append(strs[i])
            else:
                hashmap[check] = [strs[i]]
        return list(hashmap.values())