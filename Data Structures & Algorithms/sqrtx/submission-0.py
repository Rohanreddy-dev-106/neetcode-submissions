class Solution:
    def mySqrt(self, x: int) -> int:
        L=1
        R=x
        while L<=R:
            mid=L+(R-L)//2
            if mid**2==x:
                return mid
            elif mid**2 < x:
                L=mid+1
            else:
                R=mid-1
        return R
        