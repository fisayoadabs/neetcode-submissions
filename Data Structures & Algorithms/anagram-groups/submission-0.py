class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            num = ''.join(sorted(i))
            print(num)
            if(num in hashmap):
                hashmap[num].append(i)
                print(hashmap[num])
            else:
                hashmap[num] = [i]
        return list(hashmap.values())