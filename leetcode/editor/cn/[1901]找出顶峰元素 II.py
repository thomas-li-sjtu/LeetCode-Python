"""
一个 2D 网格中的 顶峰元素 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。 

 给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 顶峰元素 mat[i][j] 并 返回其位置
 [i,j] 。 

 你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。 

 要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法 

 

 

 示例 1: 

 

 
输入: mat = [[1,4],[3,2]]
输出: [0,1]
解释: 3和4都是顶峰元素，所以[1,0]和[0,1]都是可接受的答案。
 

 示例 2: 

 

 
输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
输出: [1,1]
解释: 30和32都是顶峰元素，所以[1,1]和[2,2]都是可接受的答案。
 

 

 提示： 

 
 m == mat.length 
 n == mat[i].length 
 1 <= m, n <= 500 
 1 <= mat[i][j] <= 10⁵ 
 任意两个相邻元素均不相等. 
 
 Related Topics 数组 二分查找 分治 矩阵 👍 39 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # 从任意一个点出发，可以经过一个递增路径，找到一个极大值点
        # 找到这列的最大值，然后观察其左侧右侧有没有比它大的。如果没有，那这个点就是一个全局极大值。 如果有，就说明那一侧有一个极大值点
        l, r = 0, len(mat) - 1  # 行的范围
        while l <= r:
            m = (l + r) >> 1
            localMax = max(mat[m])  # 该行最大值
            localCol = mat[m].index(localMax)  # 对应索引
            if m + 1 < len(mat) and mat[m + 1][localCol] > localMax:  # 下面更大 则说明下方存在极大值
                l = m + 1
            elif m - 1 >= 0 and mat[m - 1][localCol] > localMax:  # 上面更大 则说明上方存在极大值
                r = m - 1
            else:  # 本身更大 他就是极大值
                return [m, localCol]

# leetcode submit region end(Prohibit modification and deletion)
