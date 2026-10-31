class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            # check is the left side or ride side is sorted: this means check if the left side has rotation break else right side
            # If the left half had the rotation break inside it, the values would “wrap around” and the first value would be bigger than the last.

            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1