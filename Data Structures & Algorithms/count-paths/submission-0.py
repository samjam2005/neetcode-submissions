class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths=[1]*n
        
        for _ in range(1,m):
            for column in range(1,n):
                paths[column]+= paths[column-1]
                
        return paths[-1]