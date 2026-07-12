class Solution:
    def binarysearch(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        ans = []

        while L <= R:
            mid = L + (R - L) // 2

            # Left half is sorted
            if nums[L] <= nums[mid]:
                ans.append(min(nums[L:mid+1]))
                L = mid + 1
            else:
                # Right half is sorted
                ans.append(min(nums[mid:R+1]))
                R = mid - 1

        return min(ans) if len(ans) != 0 else -1

    def findMin(self, nums: List[int]) -> int:
         return self.binarysearch(nums)