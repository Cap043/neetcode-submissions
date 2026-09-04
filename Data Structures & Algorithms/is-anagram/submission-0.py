class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comparison={}
        for char in s:
            if char in comparison:
                comparison[char]+=1
            else:
                comparison[char]=1

        for char in t:
            if char in comparison:
                comparison[char]-=1
            else:
                return False
        for val in comparison.values():
            if val!=0:
                return False
        return True
