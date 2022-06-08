"""
给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，如果这些点构成一个 回旋镖 则返回 true 。 

 回旋镖 定义为一组三个点，这些点 各不相同 且 不在一条直线上 。 

 

 示例 1： 

 
输入：points = [[1,1],[2,3],[3,2]]
输出：true
 

 示例 2： 

 
输入：points = [[1,1],[2,2],[3,3]]
输出：false 

 

 提示： 
 

 
 points.length == 3 
 points[i].length == 2 
 0 <= xi, yi <= 100 
 
 Related Topics 几何 数组 数学 👍 42 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 三点共线向量公式
        return (points[1][0] - points[0][0]) * (points[2][1] - points[0][1]) != (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])

# leetcode submit region end(Prohibit modification and deletion)
