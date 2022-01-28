# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。 
# 
#  丑数 就是只包含质因数 2、3 和/或 5 的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1690 
#  
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 
#  👍 830 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        pt1, pt2, pt3 = 1, 1, 1
        ugly_number = [1]*(n+1)

        for i in range(2, n+1):
            ug_a, ug_b, ug_c = ugly_number[pt1]*2, ugly_number[pt2]*3, ugly_number[pt3]*5
            ugly_number[i] = min(ug_a, ug_b, ug_c)
            pt1 += 1 if ugly_number[i] == ug_a else 0
            pt2 += 1 if ugly_number[i] == ug_b else 0
            pt3 += 1 if ugly_number[i] == ug_c else 0

        return ugly_number[n]


# leetcode submit region end(Prohibit modification and deletion)
