class Solution:
    def rob(self, nums: List[int]) -> int:
        money1, money2 = 0, 0
        
        for n in nums:
            temp = max(n+money1, money2)
            money1 = money2
            money2 = temp
        return money2
            