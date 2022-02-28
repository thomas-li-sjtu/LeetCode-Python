# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i 天之后，才会有更高的温度
# 。如果气温在这之后都不会升高，请在该位置用 0 来代替。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#  
# 
#  示例 2: 
# 
#  
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#  
# 
#  示例 3: 
# 
#  
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= temperatures.length <= 105 
#  30 <= temperatures[i] <= 100 
#  
#  Related Topics 栈 数组 单调栈 
#  👍 1027 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]
        temperatures.reverse()
        stack_tem = [tuple([0, temperatures[0]])]
        for i in range(1, len(temperatures)):
            if temperatures[i] < stack_tem[-1][1]:
                res.append(i - stack_tem[-1][0])
                stack_tem.append(tuple([i, temperatures[i]]))
            else:
                while stack_tem and temperatures[i] >= stack_tem[-1][1]:
                    stack_tem.pop()
                if not stack_tem:
                    res.append(0)
                    stack_tem.append(tuple([i, temperatures[i]]))
                else:
                    res.append(i - stack_tem[-1][0])
                    stack_tem.append(tuple([i, temperatures[i]]))
        return res[::-1]

# leetcode submit region end(Prohibit modification and deletion)
