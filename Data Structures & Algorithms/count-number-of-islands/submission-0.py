class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if grid[i][j] != '0':
                grid[i][j] = '0'

                up = i-1
                right = j+1
                left = j-1
                down = i+1
                if up >= 0:
                    dfs(up,j)
                if right < n:
                    dfs(i, right)
                if left >= 0:
                    dfs(i, left)
                if down < m:
                    dfs(down, j)


        res = 0
        for i in range(m):
            for j in range(n):
                #print(grid)
                if grid[i][j] == '1':
                    #print(f"adding 1 at i, j")
                    dfs(i,j)
                    #print(grid)
                    res += 1
        return res

        