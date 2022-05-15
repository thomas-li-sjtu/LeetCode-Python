"""
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。 

 
示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释: 
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
 

 

 注意: 

 
 3 <= points.length <= 50. 
 不存在重复的点。 
 -50 <= points[i][j] <= 50. 
 结果误差值在 10^-6 以内都认为是正确答案。 
 
 Related Topics 几何 数组 数学 👍 148 👎 0

"""
from typing import List
from itertools import combinations


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2

        return max(triangleArea(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))


# leetcode submit region end(Prohibit modification and deletion)
