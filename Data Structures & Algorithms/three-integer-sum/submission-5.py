class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()


        for i, a in enumerate(nums): # a = nums[i]
            if a > 0: # since its +ve and sorted, impossible to sum 0
                break

            if i > 0 and a == nums[i - 1]: # avoid adjacent duplicates
                continue

            l, r = i + 1, len(nums) - 1 
            while l < r:
                threeSum = a + nums[l] + nums[r] # placeholder sum
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    answer.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

        return answer
        