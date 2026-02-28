class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leno = len(nums)
        sumo = sum(nums)
        missing_number = leno*(leno+1)//2 - sumo
        return missing_number