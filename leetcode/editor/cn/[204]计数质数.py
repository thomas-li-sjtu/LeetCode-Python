# 统计所有小于非负整数 n 的质数的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
# 
#  示例 2： 
# 
#  输入：n = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：n = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 5 * 106 
#  
#  Related Topics 数组 数学 枚举 数论 
#  👍 768 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        bool_nums = [0]*n
        for i in range(2, n):
            if bool_nums[i] == 0:
                j = i*2
                while j < n:
                    bool_nums[j] = 1
                    j += i
        counter = bool_nums.count(0)-2  # 去除0和1
        return counter if counter > 0 else 0
# leetcode submit region end(Prohibit modification and deletion)
