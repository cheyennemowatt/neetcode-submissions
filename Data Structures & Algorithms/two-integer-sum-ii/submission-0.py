class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non decreasing order allows for duplicates
        #O(1) spaces means no sets or dictionaries

        l, r = 0, len(numbers) -1 
        # res = [] don't use extra list
        while l < r:
            if numbers[l] + numbers[r] == target:
                #res.append(l+1)
                # res.append(r+1)
                return [l+1, r+1] #return immediately instead of appending to prevent infinite loop where l and r stay the same on the next iteration
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1
        return [] 
        
        