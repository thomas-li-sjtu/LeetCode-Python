"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 

 

 示例 1： 

 
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],[
"1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
 

 示例 2： 

 
输入：matrix = []
输出：0
 

 示例 3： 

 
输入：matrix = [["0"]]
输出：0
 

 示例 4： 

 
输入：matrix = [["1"]]
输出：1
 

 示例 5： 

 
输入：matrix = [["0","0"]]
输出：0
 

 

 提示： 

 
 rows == matrix.length 
 cols == matrix[0].length 
 1 <= row, cols <= 200 
 matrix[i][j] 为 '0' 或 '1' 
 
 Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1294 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 某一个位置，最大面积要么是往左横向区域，要么是往上竖向区域
        # （向右、向下暂时不考虑，后面的循环会解决，每个点只考虑上面和左面）
        #
        # 高:往上遍历得到
        # 宽:是随着高的遍历，每次都得到最小值——dp[i][j] = dp[i][j-1] + 1，记录当前位置的宽
        # 每次都去计算宽x高 就是面积
        # 每次都去更新面积最大值，遍历结束就得到了最大面积
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
