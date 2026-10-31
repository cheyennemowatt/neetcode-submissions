class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Brute Force
        """for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """
        #Optimal
        seen = set()
        i = 0
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False