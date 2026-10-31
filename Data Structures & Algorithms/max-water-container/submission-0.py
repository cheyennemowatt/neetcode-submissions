class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #max area
        #calculate base & height
        # move pointer if value at that pointer is smaller or equal to the value at other pointer

        l, r = 0, len(heights) -1
        max_area = 0
        area = 0

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            area = base * height
            max_area = max(max_area, area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return max_area

        
        