class Solution:
    def multp(self, key, nums):
        product = 1
        for i in range(len(nums)):#we deals with index not value
            if key != i:
                product *= nums[i]
        return product
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for key in range(len(nums)):
            if key not in hashmap:
                hashmap[key] = 1
        for key in hashmap:
            value = self.multp(key, nums)
            hashmap[key] = value

        return list(hashmap.values())