# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。 
# 
#  给定一个 整数 n， 如果是完美数，返回 true，否则返回 false 
# 
#  
# 
#  示例 1： 
# 
#  输入：28
# 输出：True
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。 
# 
#  示例 2： 
# 
#  输入：num = 6
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：num = 496
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：num = 8128
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：num = 2
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 108 
#  
#  Related Topics 数学 
#  👍 98 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        # 计数从1开始
        total = 1
        # 我们只需要判断2到int(sqrt(num))+1的数，全部累加
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                # 这里total要加上i和num // i
                total += (i + num // i)
        return total == num

# leetcode submit region end(Prohibit modification and deletion)


