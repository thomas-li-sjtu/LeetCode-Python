"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是
O(1)。 

 若队列为空，pop_front 和 max_value 需要返回 -1 

 示例 1： 

 输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
 

 示例 2： 

 输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

 

 限制： 

 
 1 <= push_back,pop_front,max_value的总操作数 <= 10000 
 1 <= value <= 10^5 
 
 Related Topics 设计 队列 单调队列 👍 375 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class MaxQueue:
    # 记住最大值出队列后，下一个最大值即可
    # 使用一个辅助队列记录最大值，每次入队时，如果deque队尾元素小于即将入队的元素value，
    # 则将小于value的元素全部出队后，再将value入队；否则直接入队

    def __init__(self):
        self.queue = []
        self.helper = []

    def max_value(self) -> int:
        return self.helper[0] if self.helper else -1

    def push_back(self, value: int) -> None:
        while self.helper and self.helper[-1] < value:
            self.helper.pop()
        self.helper.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        ans = self.queue.pop(0)
        if ans == self.helper[0]:
            self.helper.pop(0)
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
# leetcode submit region end(Prohibit modification and deletion)
