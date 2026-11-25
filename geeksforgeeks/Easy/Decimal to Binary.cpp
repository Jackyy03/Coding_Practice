class Solution:
    def decToBinary(self, n):
        s = ""
        if n == 0 :
            return "0"
        while n>0:
            rem = n%2
            s = str(rem) + s
            n = n//2
            
        return s