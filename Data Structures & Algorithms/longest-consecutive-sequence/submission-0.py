class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=list(set(nums))
        num.sort()
        longest=1
        count=1
        for i in range(1,len(num)):
            if num[i]-num[i-1]==1:
                count+=1
            else:
                count=1
            longest=max(longest,count)
        return longest