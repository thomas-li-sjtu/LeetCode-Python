"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。 

 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求： 


 
 路径途经的所有单元格都的值都是 0 。 
 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。 
 

 畅通路径的长度 是该路径途经的单元格总数。 

 

 示例 1： 

 
输入：grid = [[0,1],[1,0]]
输出：2
 

 示例 2： 

 
输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4
 

 示例 3： 

 
输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1
 

 

 提示： 

 
 n == grid.length 
 n == grid[i].length 
 1 <= n <= 100 
 grid[i][j] 为 0 或 1 
 
 Related Topics 广度优先搜索 数组 矩阵 👍 183 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        row, column = len(grid), len(grid[0])
        dir_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited = set()
        steps = []
        stack = [(0, 0, 1)]

        while stack:
            tmp_r, tmp_c, tmp_step = stack.pop(0)
            if tmp_r == row-1 and tmp_c == column-1:
                steps.append(tmp_step)
                continue
            visited.add((tmp_r, tmp_c))
            for bias_r, bias_c in dir_list:
                if 0 <= tmp_r+bias_r < row and 0 <= tmp_c+bias_c < column and \
                        grid[tmp_r+bias_r][tmp_c+bias_c] == 0 and (tmp_r+bias_r, tmp_c+bias_c) not in visited:
                    stack.append((tmp_r+bias_r, tmp_c+bias_c, tmp_step+1))
                    visited.add((tmp_r+bias_r, tmp_c+bias_c))
        return min(steps) if steps else -1

        # n = len(grid)
        # if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        #     return -1
        #
        # queue = [(0, 0, 1)]
        # # 走过的点标记为 1, 避免重复计算提高算法效率
        # grid[0][0] = 1
        # dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # for i, j, cnt in queue:
        #     if i == n - 1 and j == n - 1:
        #         return cnt
        #     for dx, dy in dir:
        #         x, y = i + dx, j + dy
        #         if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
        #             grid[x][y] = 1
        #             queue.append((x, y, cnt + 1))
        # return -1

# leetcode submit region end(Prohibit modification and deletion)
