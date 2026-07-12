class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for key in strs:
            Skey = "".join(sorted(key))
            if Skey not in hashmap:
                hashmap[Skey]=[key]
            else:
                hashmap[Skey].append(key)

        return list(hashmap.values())


        