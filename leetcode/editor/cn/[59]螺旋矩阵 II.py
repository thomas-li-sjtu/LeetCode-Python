"""
给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 

 

 示例 1： 

 
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
 

 示例 2： 

 
输入：n = 1
输出：[[1]]
 

 

 提示： 

 
 1 <= n <= 20 
 
 Related Topics 数组 矩阵 模拟 👍 670 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        round_count = n // 2

        stack = [i for i in range(1, n*n+1)]
        for i in range(round_count):
            for j in range(i, n-i):
                matrix[i][j] = stack.pop(0)
            for j in range(i+1, n-i):
                matrix[j][n-i-1] = stack.pop(0)
            for j in range(n-i-2, i-1, -1):
                matrix[n-i-1][j] = stack.pop(0)
            for j in range(n-i-2, i, -1):
                matrix[j][i] = stack.pop(0)
        if n % 2 == 1:
            matrix[n//2][n//2] = stack.pop(0)
        return matrix
# leetcode submit region end(Prohibit modification and deletion)
