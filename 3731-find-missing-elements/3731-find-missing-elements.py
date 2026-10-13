class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        min_val, max_val = min(nums), max(nums)
        
        missing = []
        for val in range(min_val + 1, max_val):
            if val not in num_set:
                missing.append(val)
                
        return missing