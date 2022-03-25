# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 104 
#  
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 1291 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            num = 10000
            for j in range(1, int(math.sqrt(i)) + 1):
                num = min(num, f[i - j ** 2])
            f[i] = num + 1
        # print(f[n])
        return f[n]

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.numSquares(7))
