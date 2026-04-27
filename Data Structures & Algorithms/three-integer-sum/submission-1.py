class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):

            # skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left += 1

                elif s > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result
        