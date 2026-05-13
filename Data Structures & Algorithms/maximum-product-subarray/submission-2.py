class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        min_prod = 1
        max_p = max(nums)

        for i in nums:
            if i == 0:
                max_prod, min_prod = 1, 1
            else:
                tmp = max_prod
                max_prod = max(i, tmp * i, min_prod * i)
                min_prod = min(i, tmp * i, min_prod * i)
                max_p = max(max_p, max_prod)

        return max_p