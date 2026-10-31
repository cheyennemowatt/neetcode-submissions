class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        """
        brute force (O(2n^2)): sum leeft side up to that number and right side after that number 
        for i in range(len(nums)):
            left_sum, right_sum = 0, 0
            for j in range(i):
                left_sum += nums[j]
            for k in range(i+1, len(nums)):
                right_sum += nums[k]
            if left_sum == right_sum:
                return i
        return -1
        """
        """
        Half optimized (O(n^2)): instead of calulatng everything after i using for loop, we can just use what we already know to find it 
        total_sum = sum(nums)

        for i in range(n):
            left_sum = 0
            for j in range(i):
                left_sum += nums[j]

            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i
        """

        total_sum = 0
        for num in nums:
            total_sum += num

        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            #instead of using a loop to calculate left_sum, we can add it everytime
            left_sum += nums[i]

        return -1


