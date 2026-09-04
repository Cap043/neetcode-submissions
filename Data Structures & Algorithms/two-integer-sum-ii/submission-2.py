class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq={}
        rem=0
        for i,n in enumerate(numbers):
            rem=target-n
            if rem in freq:
                return[freq[rem]+1,i+1]
            else:
                freq[n]=i

        