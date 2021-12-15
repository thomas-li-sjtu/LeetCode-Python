# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 104 
#  
#  Related Topics 数组 排序 
#  👍 1178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
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
