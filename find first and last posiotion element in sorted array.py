class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst):
            low, high = 0, len(nums) - 1
            bound = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        high = mid - 1  # Look left
                    else:
                        low = mid + 1   # Look right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound
        
        return [findBound(True), findBound(False)]
