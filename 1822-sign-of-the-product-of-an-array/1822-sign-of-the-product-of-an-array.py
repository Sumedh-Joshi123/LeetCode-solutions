class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        # To avoide overflow
        for i in nums:
            if i < 0:
                i = -1
            if i > 0:
                i = 1
        
        product = 1
        for i in nums:
            product *= i
            
        if product < 0:
            return -1
        
        if product > 0:
            return 1