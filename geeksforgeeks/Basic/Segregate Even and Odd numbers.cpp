class Solution:

	def segregateEvenOdd(self,arr):
	   # li = []
	    e=[]
	    o = []
	    for ele in arr:
	        if ele % 2 == 0:
	            e.append(ele)
            else:
                o.append(ele)
        e.sort()        
        o.sort()
        
        arr[:] = e + o
        return arr