"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到
达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？ 

 

 示例 1: 

 输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物 

 

 提示： 

 
 0 < grid.length <= 200 
 0 < grid[0].length <= 200 
 
 Related Topics 数组 动态规划 矩阵 👍 297 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        dp = [[grid[0][0]]]
        for i in range(1, row):
            dp.append([grid[i][0] + dp[i - 1][0]])
        for i in range(1, column):
            dp[0].append(grid[0][i] + dp[0][i-1])
            for j in range(1, row):
                dp[j].append(-1)

        for i in range(1, row):
            for j in range(1, column):
                dp[i][j] = max(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
        return dp[row-1][column-1]

# leetcode submit region end(Prohibit modification and deletion)
