class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9+7
        x = self.max_value(horizontalCuts,h)
        y = self.max_value(verticalCuts,w)
            
        return (x*y)%mod
    
    def max_value(self,array,ms):
        array.sort()
        MAX = 0
        for i,cut in enumerate(array):
            if i==0:
                MAX = max(cut,MAX)
            else:
                MAX = max(MAX,array[i]-array[i-1])
        MAX = max(MAX,ms-array[-1])
                
        return MAX