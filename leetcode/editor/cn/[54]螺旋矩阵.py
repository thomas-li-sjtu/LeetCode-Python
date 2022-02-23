# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics 数组 矩阵 模拟 
#  👍 992 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        min_length = min(len(matrix), len(matrix[0]))
        for i in range(min_length//2+1):
            new_matrix = [[matrix[j][k] for k in range(i, len(matrix[0])-i)] for j in range(i, len(matrix)-i)]
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
