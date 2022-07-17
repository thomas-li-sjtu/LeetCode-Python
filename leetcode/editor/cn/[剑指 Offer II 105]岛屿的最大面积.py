"""
给定一个由 0 和 1 组成的非空二维数组 grid ，用来表示海洋岛屿地图。 

 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（
代表水）包围着。 

 找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 

 

 示例 1: 

 

 
输入: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0
,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0
,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出: 6
解释: 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。 

 示例 2: 

 
输入: grid = [[0,0,0,0,0,0,0,0]]
输出: 0 

 

 提示： 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 50 
 grid[i][j] is either 0 or 1 
 

 

 注意：本题与主站 695 题相同： https://leetcode-cn.com/problems/max-area-of-island/ 
 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 42 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def search(i, j):
            counter = 0
            stack = [(i, j)]
            visited = {i, j}
            dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while stack:
                cur_row, cur_column = stack.pop(0)
                if grid[cur_row][cur_column] == 1:
                    counter += 1
                grid[cur_row][cur_column] = 0
                for bias_1, bias_2 in dir:
                    if 0 <= cur_row + bias_1 < row and 0 <= cur_column + bias_2 < column \
                            and grid[cur_row + bias_1][cur_column + bias_2] == 1 and (cur_row + bias_1, cur_column + bias_2) not in visited:
                        stack.append((cur_row + bias_1, cur_column + bias_2))
                        visited.add((cur_row + bias_1, cur_column + bias_2))

            return counter

        row, column = len(grid), len(grid[0])
        res = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    continue
                else:
                    res = max(search(i, j), res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
