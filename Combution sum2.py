class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results = []
        
        def backtrack(remain, combo, start):
            if remain == 0:
                results.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remain:
                    break
                
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i + 1)
                combo.pop()
        
        backtrack(target, [], 0)
        return results
