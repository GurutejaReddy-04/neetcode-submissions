class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                area = height * (i - index)
                maximum = max(maximum, area)

                start = index

            stack.append((start, h))

        # Remaining bars
        for index, height in stack:
            area = height * (len(heights) - index)
            maximum = max(maximum, area)

        return maximum