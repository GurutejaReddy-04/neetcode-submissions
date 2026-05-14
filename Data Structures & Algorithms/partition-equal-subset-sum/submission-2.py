class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2:
            return False

        target = s //2
        dp = set()
        dp.add(0)
        for i in nums:
            next_dp = set()
            for t in dp:
                if t+i == target:
                    return True
                next_dp.add(t)
                next_dp.add(t+i)
            dp = next_dp
        return False
                
                
        