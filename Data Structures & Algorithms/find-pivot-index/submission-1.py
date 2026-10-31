class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

       

        for i in range(len(nums)):
            left_sum, right_sum = 0, 0
            for j in range(i):
                left_sum += nums[j]
            for k in range(i+1, len(nums)):
                right_sum += nums[k]
            if left_sum == right_sum:
                return i
        return -1

