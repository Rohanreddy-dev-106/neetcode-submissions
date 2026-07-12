class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for ch in s:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
        for ch in t:
            if ch not in hashmap:
                return False
            hashmap[ch] -= 1
        for key in hashmap:
            if hashmap[key] != 0:
                return False

        return True