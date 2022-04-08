"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 

 
 每行中的整数从左到右按升序排列。 
 每行的第一个整数大于前一行的最后一个整数。 
 

 

 示例 1： 

 
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
 

 示例 2： 

 
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

 

 提示： 

 
 m == matrix.length 
 n == matrix[i].length 
 1 <= m, n <= 100 
 -10⁴ <= matrix[i][j], target <= 10⁴ 
 
 Related Topics 数组 二分查找 矩阵 👍 613 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                left, right = 0, len(matrix[i])-1
                while left < right:
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        left = mid+1  # 注意这里的+1和下面的-1！
                    if matrix[i][mid] > target:
                        right = mid-1
                if left == right and matrix[i][left] == target:
                    return True
                else:
                    return False
            else:
                continue
        return False
# leetcode submit region end(Prohibit modification and deletion)
