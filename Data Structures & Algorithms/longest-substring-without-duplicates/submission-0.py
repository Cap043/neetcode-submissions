class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        result=0
        charset=set(
        )
        for i in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            right+=1
            result=max(result,right-left)
        return result