class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        
        def backtrack(start):
            if start == len(nums):
                results.append(list(nums))
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return results
