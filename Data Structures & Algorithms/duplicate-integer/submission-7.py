class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

       # False example: [1,2,3,4]
       # True example: [1,2,3,1]

       #Input: array
       #Output boolean value (true or false)
       #appears: we shoudl be scanning the list using a for loop
       #more than once: try set 


        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            else:
                seen.add(elem)

        return False
