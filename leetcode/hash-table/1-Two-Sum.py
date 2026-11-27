class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        dic ={}

        for i in range(n):
            rem  = target - nums[i]
            if rem in dic:
                return [dic[rem],i]
            else:
                dic[nums[i]] = i