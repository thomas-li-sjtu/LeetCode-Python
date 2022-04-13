"""
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。 

 

 示例 1： 

 
输入：points = [[1,1],[2,2],[3,3]]
输出：3
 

 示例 2： 

 
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
 

 

 提示： 

 
 1 <= points.length <= 300 
 points[i].length == 2 
 -10⁴ <= xi, yi <= 10⁴ 
 points 中的所有点 互不相同 
 
 Related Topics 几何 数组 哈希表 数学 👍 402 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        res = 2
        n = len(points)
        for i in range(n):
            lines = {}
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, n):
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2:
                    a, b, c = 1, 0, -x1
                elif y1 == y2:
                    a, b, c = 0, 1, -y1
                else:
                    a = 1.0
                    b = 1.0 * (x1 - x2) / (y2 - y1)
                    c = 1.0 * (x1 * y2 - x2 * y1) / (y1 - y2)

                if lines.get((a, b, c)):
                    lines[(a, b, c)] += 1
                    res = max(res, lines[(a, b, c)])
                else:
                    lines[(a, b, c)] = 2
        return res
