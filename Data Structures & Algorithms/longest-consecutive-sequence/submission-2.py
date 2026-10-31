class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        tracker = set(nums)
        dup = set()
        count = 0

        for num in nums:
            if num + 1 in tracker and num not in dup:
                count +=1
                dup.add(num)
        return count
        """
        #Only start counting a sequence if the number has no predecessor.
        
        # the first number we see counts so start at 1
        # we don't want to account for duplicates in our final count so use a varaible to hold the number were checking and update it by 1 everytime
        # since we can get an empty array, we should set max length to 0 
        # we check if each number in the set : 
        #put len = 1 in the for loop for when we need to restart our count
        # use a while loop that continues to see if the next number is set , update length, 
        # once we hit a condition where its not, we see if that number if the max
        # return the max


        max_count = 0

        for num in nums:
            count = 1
            current_num = num 
            while current_num + 1 in nums:
                count +=1
                current_num +=1 # we want to actually move on to the next number and not just keep checking same condition again
            max_count = max(count, max_count)
        
        return max_count
        

        
        
        

