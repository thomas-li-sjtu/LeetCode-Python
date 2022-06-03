"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下： 

 
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 

 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。 

 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 

 

 示例 1： 

 
输入：n = 2
输出：1
 

 示例 2： 

 
输入：n = 5
输出：5
 

 

 提示： 

 
 0 <= n <= 100 
 
 Related Topics 记忆化搜索 数学 动态规划 👍 366 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        res = [0, 1]
        if n == 0 or n == 1:
            return res[n]
        else:
            for _ in range(2, n+1):
                res.append(res[-2] + res[-1])
            return res[n] % 1000000007
# leetcode submit region end(Prohibit modification and deletion)

