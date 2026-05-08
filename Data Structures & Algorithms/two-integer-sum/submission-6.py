class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # hash map

        for i, n in enumerate(nums): # index - val
            diff = target - n
            if diff in seen:
                return [seen[diff], i] # return index of diff and current
            else:
                seen[n] = i
        
        