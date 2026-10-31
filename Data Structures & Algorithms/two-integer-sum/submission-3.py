class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #input: nums array & target integer
    #output: [i,j]
    
        index = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]




    