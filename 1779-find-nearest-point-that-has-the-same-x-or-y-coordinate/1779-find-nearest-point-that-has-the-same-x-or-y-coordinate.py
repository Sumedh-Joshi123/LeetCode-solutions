class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDis = 10**10
        minDis_i = -1
        
        for index, (x1,y1) in enumerate(points):
            if x == x1 or y == y1:
                dist = abs(x-x1)+abs(y-y1)
                
                if dist<minDis:
                    minDis_i = index
                    minDis = dist
                    
        return minDis_i
        
        