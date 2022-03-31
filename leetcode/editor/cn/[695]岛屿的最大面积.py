"""
给你一个大小为 m x n 的二进制矩阵 grid 。 

 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 
0（代表水）包围着。 

 岛屿的面积是岛上值为 1 的单元格的数目。 

 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 

 

 示例 1： 

 
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,
0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,
0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
 

 示例 2： 

 
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0
 

 

 提示： 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 50 
 grid[i][j] 为 0 或 1 
 
 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 737 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        island_visited = set()

        row, column = len(grid), len(grid[0])
        dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # def search_island(grid, visited, island_visited, i, j):
        #
        #
        #     return len(island_visited)

        for i in range(row):
            for j in range(column):
                if (i, j) not in visited:
                    visited.add((i, j))
                    if grid[i][j] == 1:
                        stack = [(i, j)]
                        while stack:
                            i, j = stack.pop(0)
                            island_visited.add((i, j))
                            for add_r, add_c in dir_list:
                                if 0 <= i + add_r < row and 0 <= j + add_c < column \
                                        and grid[i + add_r][j + add_c] == 1 and (i + add_r, j + add_c) not in island_visited:
                                    island_visited.add((i + add_r, j + add_c))
                                    stack.append((i+add_r, j+add_c))

                        max_area = max(max_area, len(island_visited))
                        print(island_visited)
                        island_visited = set()
        return max_area
# leetcode submit region end(Prohibit modification and deletion)
