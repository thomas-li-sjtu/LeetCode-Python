"""
有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。 

 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元
格 高于海平面的高度 。 

 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。 

 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。
 

 

 示例 1： 

 

 
输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
 

 示例 2： 

 
输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]
 

 

 提示： 

 
 m == heights.length 
 n == heights[r].length 
 1 <= m, n <= 200 
 0 <= heights[r][c] <= 10⁵ 
 
 Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 387 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.pacific = set()
        self.atlantic = set()
        self.visited = set()
        self.direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 找出所有从太平洋出发的水所能达到的点
        # 找出所有从大西洋出发的水所能达到的点
        # 重合的点便是要找的点
        res = []
        row, column = len(heights), len(heights[0])
        start_pacific = [(i, j) for i in range(row) for j in range(column) if i == 0 or j == 0]
        start_atlantic = [(i, j) for i in range(row) for j in range(column) if i == row - 1 or j == column - 1]

        self.bfs(start_pacific, "pacific", heights, row, column)
        self.visited = set()
        self.bfs(start_atlantic, "atlantic", heights, row, column)

        for i in self.pacific:
            if i in self.atlantic:
                res.append(i)
        return res

    def bfs(self, stack, ocean_type, heights, row, column):
        while stack:
            tmp = stack.pop(0)
            self.visited.add(tmp)
            if ocean_type == "atlantic":
                self.atlantic.add(tmp)
            if ocean_type == "pacific":
                self.pacific.add(tmp)
            tmp_water = heights[tmp[0]][tmp[1]]
            for i, j in self.direction:
                if 0 <= tmp[0] + i < row and 0 <= tmp[1] + j < column and \
                        tmp_water <= heights[tmp[0] + i][tmp[1] + j] and (tmp[0] + i, tmp[1] + j) not in self.visited:
                    stack.append((tmp[0] + i, tmp[1] + j))


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.pacificAtlantic(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
