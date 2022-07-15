"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 

 说明：一个机器人每次只能向下或者向右移动一步。 

 

 示例 1： 

 

 
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
 

 示例 2： 

 
输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

 

 提示： 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 200 
 0 <= grid[i][j] <= 100 
 

 

 注意：本题与主站 64 题相同： https://leetcode-cn.com/problems/minimum-path-sum/ 
 Related Topics 数组 动态规划 矩阵 👍 23 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for j in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
