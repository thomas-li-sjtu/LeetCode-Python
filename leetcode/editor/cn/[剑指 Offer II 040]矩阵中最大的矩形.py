"""
给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。 

 注意：此题 matrix 输入格式为一维 01 字符串数组。 

 

 示例 1： 

 

 
输入：matrix = ["10100","10111","11111","10010"]
输出：6
解释：最大矩形如上图所示。
 

 示例 2： 

 
输入：matrix = []
输出：0
 

 示例 3： 

 
输入：matrix = ["0"]
输出：0
 

 示例 4： 

 
输入：matrix = ["1"]
输出：1
 

 示例 5： 

 
输入：matrix = ["00"]
输出：0
 

 

 提示： 

 
 rows == matrix.length 
 cols == matrix[0].length 
 0 <= row, cols <= 200 
 matrix[i][j] 为 '0' 或 '1' 
 

 

 注意：本题与主站 85 题相同（输入参数格式不同）： https://leetcode-cn.com/problems/maximal-rectangle/ 

 Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 49 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        if not matrix:
            return 0
        matrix = [list(i) for i in matrix]
        row, column = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(column)] for j in range(row)]

        res = 0
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if j > 0:
                        dp[i][j] = dp[i][j-1] + 1
                    width = dp[i][j]
                    for k in range(i, -1, -1):
                        width = min(width, dp[k][j])
                        if width == 0:
                            break
                        res = max(res, width*(i-k+1))
        return res
# leetcode submit region end(Prohibit modification and deletion)
