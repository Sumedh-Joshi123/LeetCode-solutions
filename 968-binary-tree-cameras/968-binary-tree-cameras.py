# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return False, True
            c1,m1 = dfs(node.left)
            c2,m2 = dfs(node.right)
            
            camera, moniter = False, False
            if c1 or c2:
                moniter = True
            if not m1 or not m2:
                camera = True
                self.result += 1
                moniter = True
                
            return camera, moniter
        
        c,m = dfs(root)
        if not m: return self.result + 1
        
        return self.result
            