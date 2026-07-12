from typing import List

class Solution:
    def binarysearch(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[L] <= nums[mid]:
                if nums[L] <= target <=nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <=target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums, target)