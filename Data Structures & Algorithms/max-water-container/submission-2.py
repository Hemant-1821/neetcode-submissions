class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j  = 0, len(heights)-1
        highest_area = 0
        while i < j:
            curr_area = (j-i) * min(heights[i], heights[j])
            highest_area = max(highest_area, curr_area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return highest_area