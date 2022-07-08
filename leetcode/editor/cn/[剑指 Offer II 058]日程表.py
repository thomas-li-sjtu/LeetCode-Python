"""
请实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。 

 MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时
间是半开区间，即 [start, end), 实数 x 的范围为， start <= x < end。 

 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。 

 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true。否则，返回 false 并且不要将该日程
安排添加到日历中。 

 请按照以下步骤调用 MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(
start, end) 

 

 示例: 

 
输入:
["MyCalendar","book","book","book"]
[[],[10,20],[15,25],[20,30]]
输出: [null,true,false,true]
解释: 
MyCalendar myCalendar = new MyCalendar();
MyCalendar.book(10, 20); // returns true 
MyCalendar.book(15, 25); // returns false ，第二个日程安排不能添加到日历中，因为时间 15 已经被第一个日程安排预定了

MyCalendar.book(20, 30); // returns true ，第三个日程安排可以添加到日历中，因为第一个日程安排并不包含时间 20 
 

 

 

 提示： 

 
 每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。 
 0 <= start < end <= 10⁹ 
 

 

 注意：本题与主站 729 题相同： https://leetcode-cn.com/problems/my-calendar-i/ 
 Related Topics 设计 线段树 二分查找 有序集合 👍 31 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        # 情况1：第一次book
        if not self.cal:
            self.cal.append([start, end])
            return True

        # sp:start_position, 二分查找start的插入点（在这之前不需要sort因为每次插入都是排序插入的）
        sp = bisect.bisect_left(self.cal, [start, end])

        # 情况2：sp > 0 保证 sp-1 索引有效。start < 前一项的 end，有重叠返回 False
        if sp > 0 and start < self.cal[sp - 1][1]:
            return False

        # 情况3：sp < len(self.cal) 保证 sp 索引有效。end > 后一项的 start，有重叠返回 False
        if sp < len(self.cal) and end > self.cal[sp][0]:
            return False

        # 其他情况：在插入点插入[start, end]，返回 True
        self.cal[sp:sp] = [[start, end]]
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)
