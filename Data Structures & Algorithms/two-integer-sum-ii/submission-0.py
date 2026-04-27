class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(numbers)):
            num = numbers[i]
            complement = target - num
            
            if complement in seen:
                return [seen[complement] +1, i+1]
            
            seen[num] = i
            