class Solution: 
    def lessThan(self, arr, k):
        li = []
        for ele in arr:
            if ele <k:
                li.append(ele)
        return(li)