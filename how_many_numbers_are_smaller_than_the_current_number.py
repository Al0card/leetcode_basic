class Solution:
    def smallerNumbersThanCurrent(self, nums):
        s_nums = sorted(nums)
        seen = {}
        result = []
        for i, x in enumerate(s_nums):
            if x not in seen:
                seen[x] = i
        for i in nums:
            result.append(seen[i])
        return result