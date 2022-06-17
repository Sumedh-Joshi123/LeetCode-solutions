class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = [int(a) for a in str(n)]
        Product = 1
        Sum = 0
        for i in x:
            Product *= i
            Sum += i
            
        return (Product-Sum)