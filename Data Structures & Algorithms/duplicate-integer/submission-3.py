class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map={}
        for i in nums:
            if i in freq_map:
               freq_map[i]=freq_map[i]+1
            else:
                freq_map[i]=1
        for key in freq_map.keys():
            if freq_map[key]>1:
               return True
        return False
        