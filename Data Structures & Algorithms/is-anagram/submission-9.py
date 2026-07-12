class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for key in t:
            if key in hashmap:
                hashmap[key]=hashmap[key] -1
        for key in hashmap.keys():
            if hashmap[key] != 0:
                return False

        return True