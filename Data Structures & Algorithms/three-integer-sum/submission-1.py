class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])

                if target in seen:
                    t = sorted([nums[i], nums[j], target])
                    if t not in ans:
                        ans.append(t)

                seen.add(nums[j])

        return ans