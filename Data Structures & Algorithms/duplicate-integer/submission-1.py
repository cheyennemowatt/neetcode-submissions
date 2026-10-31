class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for elem in nums:
            if elem not in seen:
                seen.add(elem)
            else:
                return True
        return False
     