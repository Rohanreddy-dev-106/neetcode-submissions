from typing import List

class Solution:
    def search(self, nums, target):
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.search(row, target) != -1:
                return True
        return False