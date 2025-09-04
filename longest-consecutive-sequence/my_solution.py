class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        nums = set(nums) 
        for i, val in enumerate(nums):
            dict[val] = 0
        lcs = []
        idx = 0
        max = 0
        for i in nums:
            if i-1 not in dict:
                while((i+idx) in dict):
                    idx += 1
                    
                if idx > max:
                    max = idx
                idx = 0
        return max

