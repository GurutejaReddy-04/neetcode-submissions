class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        for i in range(len(nums) - k + 1):
            window_max = nums[i]

            for j in range(i, i + k):
                window_max = max(window_max, nums[j])

            result.append(window_max)

        return result
        