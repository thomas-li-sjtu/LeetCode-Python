# 图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。 
# 
#  每个单元格的 平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。 
# 
#  如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。 
# 
#  
# 
#  给你一个表示图像灰度的 m x n 整数矩阵 img ，返回对图像的每个单元格平滑处理后的图像 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入:img = [[1,1,1],[1,0,1],[1,1,1]]
# 输出:[[0, 0, 0],[0, 0, 0], [0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
#  
# 
#  示例 2: 
# 
#  
# 输入: img = [[100,200,100],[200,50,200],[100,200,100]]
# 输出: [[137,141,137],[141,138,141],[137,141,137]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
# 
# 对于点 (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.
# 666667) = 141
# 对于点 (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) =
#  138
#  
# 
#  
# 
#  提示: 
# 
#  
#  m == img.length 
#  n == img[i].length 
#  1 <= m, n <= 200 
#  0 <= img[i][j] <= 255 
#  
#  Related Topics 数组 矩阵 
#  👍 140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        import copy
        res = copy.deepcopy(img)
        m = len(res)
        n = len(res[0])

        if m >= 2 and n >= 2:
            for i in range(m):
                for j in range(n):
                    if 0 < i < m - 1 and 0 < j < n-1:
                        sum = img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j] + img[i][j-1] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1]
                        res[i][j] = sum // 9
                    elif i == 0 and j == 0:
                        res[i][j] = (img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1]) // 4
                    elif i == m-1 and j == n-1:
                        res[i][j] = (img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1]) // 4
                    elif i == 0 and j == n-1:
                        res[i][j] = (img[i][j] + img[i][j-1] + img[i+1][j] + img[i+1][j-1]) // 4
                    elif i == m-1 and j == 0:
                        res[i][j] = (img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1]) // 4
                    elif 0 < i < m - 1 and j == n-1:
                        res[i][j] = (img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1] + img[i+1][j] + img[i+1][j-1]) // 6
                    elif 0 < i < m - 1 and j == 0:
                        res[i][j] = (img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1] + img[i+1][j] + img[i+1][j+1]) // 6
                    elif i == 0 and 0 < j < n-1:
                        res[i][j] = (img[i][j] + img[i][j+1] + img[i][j-1] + img[i+1][j] + img[i+1][j+1] + img[i+1][j-1]) // 6
                    elif i == m-1 and 0 < j < n-1:
                        res[i][j] = (img[i][j] + img[i][j+1] + img[i][j-1] + img[i-1][j] + img[i-1][j+1] + img[i-1][j-1]) // 6
        elif m == 1 and n == 1:
            return res
        elif m == 1:
            for i in range(n):
                if i == 0:
                    res[0][i] = (img[0][i] + img[0][i+1]) // 2
                elif i == n-1:
                    res[0][i] = (img[0][i] + img[0][i-1]) // 2
                else:
                    res[0][i] = (img[0][i-1] + img[0][i] + img[0][i+1]) // 3
        elif n == 1:
            for i in range(m):
                if i == 0:
                    res[i][0] = (img[i][0] + img[i+1][0]) // 2
                elif i == m-1:
                    res[i][0] = (img[i][0] + img[i-1][0]) // 2
                else:
                    res[i][0] = (img[i-1][0] + img[i][0] + img[i+1][0]) // 3
        return res
# leetcode submit region end(Prohibit modification and deletion)
