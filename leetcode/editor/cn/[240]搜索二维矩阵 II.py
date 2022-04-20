"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性： 

 
 每行的元素从左到右升序排列。 
 每列的元素从上到下升序排列。 
 

 

 示例 1： 

 
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,2
3,26,30]], target = 5
输出：true
 

 示例 2： 

 
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,2
3,26,30]], target = 20
输出：false
 

 

 提示： 

 
 m == matrix.length 
 n == matrix[i].length 
 1 <= n, m <= 300 
 -10⁹ <= matrix[i][j] <= 10⁹ 
 每行的所有元素从左到右升序排列 
 每列的所有元素从上到下升序排列 
 -10⁹ <= target <= 10⁹ 
 
 Related Topics 数组 二分查找 分治 矩阵 👍 990 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 若左下角元素等于目标，则找到
        # 若左下角元素大于目标，则目标不可能存在于当前矩阵的最后一行，问题规模可以减小为在去掉最后一行的子矩阵中寻找目标
        # 若左下角元素小于目标，则目标不可能存在于当前矩阵的第一列，问题规模可以减小为在去掉第一列的子矩阵中寻找目标
        row, column = len(matrix), len(matrix[0])
        cur = [row-1, 0]
        while 0 <= cur[0] < row and 0 <= cur[1] < column:
            if matrix[cur[0]][cur[1]] == target:
                return True
            elif matrix[cur[0]][cur[1]] > target:
                cur[0] -= 1
            elif matrix[cur[0]][cur[1]] < target:
                cur[1] += 1
            print(cur)

        return False
# leetcode submit region end(Prohibit modification and deletion)
