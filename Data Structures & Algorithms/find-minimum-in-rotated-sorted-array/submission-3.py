class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        instead of comparing numbers at left and right (“Which pointer should I move?”) we compare numbers at middle and right (“Which HALF can I safely throw away?”)
        if the number at the middle is bigger than the number at the right, then the smallest has to be to the right of mid
        if the number at the middle is smaller or equal, it has to be at the mid or to the left
        nums[mid] > nums[r] does not mean “mid is bigger than right” means “mid is in the LEFT chunk, not the sorted RIGHT chunk”
        right side is always ordered, left may be roken by rotation
        The right side is sorted.
If mid is bigger than right, it’s not in that sorted side.
So the minimum must be on the other side.

        eventually we reach a point where l == r so we can return nums[l] as smallest
        Key: Rotated array -> compare mid with right
        """

        # “Keep going only while there are at least TWO candidates left.”
        #When l == r, we stop We not touch that last remaining index
        #That index is the answer
        #l<=r would keep reprocessing last one creating infinite loop
        

        l, r = 0, len(nums) -1

        while l < r:
            mid = (l+r) //2
            # doesn't matter if you put >= or > because nums[mid] == nums[r] can only happen when mid == r and that only happens when the loop will end anyway so it doesn't matter
            if nums[mid] >= nums[r]:
               l= mid +1
            else:
                r = mid
        return nums[l] 