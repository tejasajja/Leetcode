class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        maxans=float('-inf')
        setx=set()
        l=0
        for r in range(len(s)):
            if s[r] in setx:
                while l<r and s[r] in setx:
                    setx.remove(s[l])
                    l+=1
            setx.add(s[r])
            maxans=max(maxans, r-l+1)
        return maxans




        

                