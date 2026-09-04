class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        r=max(piles)
        while l<=r:
            count=0
            mid=l+(r-l)//2
            for n in piles:
                count+=(n+mid-1)//mid
                result=mid
            if count<=h:
                r=mid-1
            else:
                l=mid+1
        return l
                