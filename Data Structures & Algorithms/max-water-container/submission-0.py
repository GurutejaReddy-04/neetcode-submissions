class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right = n - 1
        area = 0

        while left < right:
            cur_area = min(heights[left], heights[right]) * (right - left)
            area = max(area, cur_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area



        