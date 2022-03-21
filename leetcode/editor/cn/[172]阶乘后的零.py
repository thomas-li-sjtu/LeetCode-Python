# 给定一个整数 n ，返回 n! 结果中尾随零的数量。 
# 
#  提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 104 
#  
# 
#  
# 
#  进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？ 
#  Related Topics 数学 
#  👍 559 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter_2, counter_5 = 0, 0
        for i in range(2, n+1):
            while i % 2 == 0:
                i /= 2
                counter_2 += 1
            while i % 5 == 0:
                i /= 5
                counter_5 += 1
        return min(counter_5, counter_2)
# leetcode submit region end(Prohibit modification and deletion)
