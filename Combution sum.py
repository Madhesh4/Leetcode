class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        
        def backtrack(remain, combo, start_idx):
            # Base Case: Target reached
            if remain == 0:
                results.append(list(combo))
                return
            # Base Case: Exceeded target or exhausted candidates
            if remain < 0:
                return
            
            for i in range(start_idx, len(candidates)):
                # 1. Add the number to the current combination
                combo.append(candidates[i])
                
                # 2. Recurse. Note: index stays 'i' because we can reuse candidates[i]
                backtrack(remain - candidates[i], combo, i)
                
                # 3. Remove the number (backtrack) to try the next candidate
                combo.pop()
        
        backtrack(target, [], 0)
        return results
