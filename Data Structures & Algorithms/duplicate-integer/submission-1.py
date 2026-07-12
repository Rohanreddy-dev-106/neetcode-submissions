class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for key in nums:
            if key not in hashmap:
                hashmap[key] = 1
            else:
                hashmap[key] = hashmap[key] + 1 

        for key in hashmap:
            if hashmap[key] > 1:
                return True
        return False