class Solution:
    def claculatemink(self, piles, k):
        total_hours = 0
        for p in piles:                     
            total_hours += math.ceil(p / k)
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = -1
        # for k in range(1, max(piles) + 1):   
        #     if self.claculatemink(piles, k) <= h:#kbananas per 1 hour
        #         ans = k                      
        #         break                        
        # return ans
        L=1
        R=max(piles)
        while(L<=R):
            mid=L+(R-L)//2
            if self.claculatemink(piles,mid)<=h:
                ans=mid
                R=mid-1
            elif self.claculatemink(piles,mid) > h:
                L=mid+1
        return ans