class Solution:
    def reverseString(self, s: str) -> str:
        rev = ""
        n = len(s)
        for i in range(n):
            rev += s[-1]
            s = s[:-1]
        return rev
