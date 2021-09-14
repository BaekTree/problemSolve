#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s, i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
        
    def helper(self, s, j,k):
        
        while j > 0 and k < len(s)-1 and s[j] == s[k]:
            j = j - 1
            k = k + 1
        j += 1
        k -= 1
        
        return s[j:k+1]
    
                
            
