class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(len(nums)):
            product = 1
            for j in range(i):
                product *= nums[j]
            for k in range(i+1, len(nums)):
                product *= nums[k]
            output.append(product)
        return output


        