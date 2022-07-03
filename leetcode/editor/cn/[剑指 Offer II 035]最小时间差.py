"""
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 

 

 示例 1： 

 
输入：timePoints = ["23:59","00:00"]
输出：1
 

 示例 2： 

 
输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 

 

 提示： 

 
 2 <= timePoints <= 2 * 10⁴ 
 timePoints[i] 格式为 "HH:MM" 
 

 

 注意：本题与主站 539 题相同： https://leetcode-cn.com/problems/minimum-time-difference/ 
 Related Topics 数组 数学 字符串 排序 👍 21 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []

        for i in timePoints:
            hour, minute = int(i.split(":")[0]), int(i.split(":")[1])
            time.append(hour * 60 + minute)
        time.sort()

        return min([time[i] - time[i - 1] for i in range(1, len(time))] + [time[0] + 24 * 60 - time[-1]])
# leetcode submit region end(Prohibit modification and deletion)
