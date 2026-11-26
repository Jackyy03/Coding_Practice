class Solution:
    def decrementArray(self, arr: list[int], n: int) -> list[int]:
        li = []
        for ele in arr:
             li.append(ele-1)
        return li
        