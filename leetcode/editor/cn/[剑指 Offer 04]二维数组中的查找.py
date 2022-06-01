"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数
，判断数组中是否含有该整数。 

 

 示例: 

 现有矩阵 matrix 如下： 

 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
 

 给定 target = 5，返回 true。 

 给定 target = 20，返回 false。 

 

 限制： 

 0 <= n <= 1000 

 0 <= m <= 1000 

 

 注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 
 Related Topics 数组 二分查找 分治 矩阵 👍 684 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 从左下开始
        if not matrix:
            return False
        tmp_row, tmp_column = len(matrix)-1, 0
        while tmp_row >= 0 and tmp_column <= len(matrix[0])-1:
            if matrix[tmp_row][tmp_column] == target:
                return True
            elif matrix[tmp_row][tmp_column] < target:
                tmp_column += 1
            else:
                tmp_row -= 1
        return False

        # # 从右上开始（站在右上角看。这个矩阵其实就像是一个Binary Search Tree）
        # if not matrix:
        #     return False
        # tmp_row, tmp_column = 0, len(matrix[0])-1
        # while tmp_row <= len(matrix)-1 and tmp_column >= 0:
        #     if matrix[tmp_row][tmp_column] == target:
        #         return True
        #     elif matrix[tmp_row][tmp_column] > target:
        #         tmp_column -= 1
        #     else:
        #         tmp_row += 1
        # return False

# leetcode submit region end(Prohibit modification and deletion)
