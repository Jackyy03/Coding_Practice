class Solution:
    def isPalindrome(self, s):
        
        s = s.lower()
        rev = ""
        
        for ch in s:
            rev = ch + rev
        
        if rev == s:
            return True
        else:
            return False