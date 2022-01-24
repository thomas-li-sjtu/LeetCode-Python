# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[0].length 
#  1 <= m, n <= 200 
#  -231 <= matrix[i][j] <= 231 - 1 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  一个直观的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。 
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。 
#  你能想出一个仅使用常量空间的解决方案吗？ 
#  
#  Related Topics 数组 哈希表 矩阵 
#  👍 641 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        location = []
        for index_l, line in enumerate(matrix):
            set_zero = 0
            for index_r, char in enumerate(line):
                if char == 0:
                    location.append([index_l, index_r])
                    set_zero = 1
            if set_zero:
                for index_r, char in enumerate(line):
                    matrix[index_l][index_r] = 0

        for loca in location:
            for index_l, line in enumerate(matrix):
                for index_r, char in enumerate(line):
                    if index_r == loca[1]:
                        matrix[index_l][index_r] = 0
                        break

# leetcode submit region end(Prohibit modification and deletion)
