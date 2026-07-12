class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        count=0
        for i in nums:
            if i in hashmap:
                hashmap[i]=hashmap[i]+1
            else:
                hashmap[i]=1
        for key in hashmap.keys():
            if hashmap[key] > 1:
                count+=1
        return count >=1

        