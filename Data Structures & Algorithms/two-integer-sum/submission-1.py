class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Make a Hashmap for every value in list
        
        #Hashmap will map each value to each index
        seen = {}

        #Check target - nums[i], if doesn't exist in hashmap add to hashmap with nums[i] as key and index as value
        #continue to iterate through list 
        
        #i is index and num is the actual number
        #enumerate gives index, value pairs
        for i , num in enumerate (nums):
            difference = target - num
            if difference in seen:
                #don't just return num bc we need indices of the difference num not value
                return [seen[difference], i]
            #update value (index) for the key if it appears later in the list
            seen[num] = i
    