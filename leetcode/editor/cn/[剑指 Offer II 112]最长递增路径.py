"""
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。 

 对于每个单元格，你可以往上，下，左，右四个方向移动。 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。 

 

 示例 1： 

 

 
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。 

 示例 2： 

 

 
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
 

 示例 3： 

 
输入：matrix = [[1]]
输出：1
 

 

 提示： 

 
 m == matrix.length 
 n == matrix[i].length 
 1 <= m, n <= 200 
 0 <= matrix[i][j] <= 2³¹ - 1 
 

 

 注意：本题与主站 329 题相同： https://leetcode-cn.com/problems/longest-increasing-path-in-
a-matrix/ 
 Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 记忆化搜索 数组 动态规划 矩阵 👍 23 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(row: int, column: int) -> int:
            if self.memo[row][column] != 0:
                return self.memo[row][column]
            self.memo[row][column] = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    self.memo[row][column] = max(self.memo[row][column], dfs(newRow, newColumn)+1)
            return self.memo[row][column]

        self.memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        if not matrix:
            return 0
        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
