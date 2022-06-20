class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        while n!=1:
            n = sum([int(x)**2 for x in str(n)])
            if n in arr:
                return False
            arr.append(n)
        return True    
        
            