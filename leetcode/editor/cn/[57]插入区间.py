# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。 
# 
#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。 
# 
#  示例 3： 
# 
#  
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
#  
# 
#  示例 4： 
# 
#  
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
#  
# 
#  示例 5： 
# 
#  
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= intervals[i][0] <= intervals[i][1] <= 105 
#  intervals 根据 intervals[i][0] 按 升序 排列 
#  newInterval.length == 2 
#  0 <= newInterval[0] <= newInterval[1] <= 105 
#  
#  Related Topics 数组 
#  👍 550 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 首先，基于每个子数组的start排序——要取最左边界和最右边界，左边界通过排序，右边界通过比较。
        # 将排序后的intervals[0]的左右端点当做start和end，之后从1 - len(intervals)开始比较。
        # 当intervals[i][0] > end, 标识此处断开。此时将start和end加入ret待返回的数组。
        # 当intervals[i][0] < end, 标识此处未断开。此时end应该等于max(end, intervals[i][1])
        # intervals[i]的左右边界作为新的start和end。
        # 持续上面操作，直到数组遍历结束。此时最后一个数组没有比较，则直接将start和当前的end加入ret待返回数组

        ret = []
        intervals.sort()
        start, end = intervals[0]
        for i in intervals:
            if i[0] > end:
                ret.append([start, end])
                start = i[0]
            end = max(end, i[1])
        ret.append([start, end])
        return ret
# leetcode submit region end(Prohibit modification and deletion)
#
s = Solution()
print(s.insert([[1,5], [5, 7]], [2,5]))