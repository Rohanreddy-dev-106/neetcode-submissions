class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for key in hashmap:
            if hashmap[key] > 1:
                return key