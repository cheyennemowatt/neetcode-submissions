class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #input: nums array & target integer
    #output: [i,j]
    
        index = {}

        for i in range (len(nums)):
            difference = target - nums[i]
            if difference in index:
                return [index[difference], i]
            index[nums[i]] = i 




    