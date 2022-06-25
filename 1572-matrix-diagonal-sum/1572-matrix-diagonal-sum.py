class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        length = len(mat)
        for i in range(length):
            ans += mat[i][i]
            if (i,i) != (i, length-i-1):
                ans += mat[i][length-i-1]
                
        return ans