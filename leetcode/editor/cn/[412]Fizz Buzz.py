# 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中： 
# 
#  
#  answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。 
#  answer[i] == "Fizz" 如果 i 是 3 的倍数。 
#  answer[i] == "Buzz" 如果 i 是 5 的倍数。 
#  answer[i] == i （以字符串形式）如果上述条件全不满足。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["1","2","Fizz"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：["1","2","Fizz","4","Buzz"]
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 15
# 输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","1
# 4","FizzBuzz"] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 104 
#  
#  Related Topics 数学 字符串 模拟 
#  👍 160 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out
# leetcode submit region end(Prohibit modification and deletion)
