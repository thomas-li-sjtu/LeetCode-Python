"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 

 

 示例 1： 

 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
 

 示例 2： 

 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

 

 限制： 

 
 0 <= matrix.length <= 100 
 0 <= matrix[i].length <= 100 
 

 注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
 Related Topics 数组 矩阵 模拟 👍 415 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        min_length = min(len(matrix), len(matrix[0]))
        for i in range(min_length // 2 + 1):
            new_matrix = [[matrix[j][k] for k in range(i, len(matrix[0]) - i)] for j in range(i, len(matrix) - i)]
            if new_matrix:
                res.extend(self.out_round(new_matrix))
        return res

    def out_round(self, matrix):
        res = []
        if len(matrix) > 1 and len(matrix[0]) > 1:
            for i in range(len(matrix[0])):
                res.append(matrix[0][i])
            for i in range(1, len(matrix)):
                res.append(matrix[i][len(matrix[0]) - 1])
            for i in range(len(matrix[0]) - 2, -1, -1):
                res.append(matrix[-1][i])
            for i in range(len(matrix) - 2, 0, -1):
                res.append(matrix[i][0])
        else:
            if len(matrix) == 1 and len(matrix[0]) >= 1:
                res.extend(matrix[0])
            elif len(matrix) > 1 and len(matrix[0]) == 1:
                res.extend([i[0] for i in matrix])
        return res
# leetcode submit region end(Prohibit modification and deletion)
