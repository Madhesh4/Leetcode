from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        results = []
        counts = Counter(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                results.append(list(path))
                return
            
            for num in counts:
                if counts[num] > 0:
                    path.append(num)
                    counts[num] -= 1
                    
                    backtrack(path)
                    
                    counts[num] += 1
                    path.pop()
                    
        backtrack([])
        return results
