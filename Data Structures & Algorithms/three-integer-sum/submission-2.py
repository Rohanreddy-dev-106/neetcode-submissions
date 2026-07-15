class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t=[nums[i], nums[j], nums[k]]
                        t.sort()
                        if t in ans:
                            continue
                        ans.append(t)
                        
        return ans