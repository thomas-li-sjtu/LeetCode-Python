# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。 
# 
#  示例: 
# 
#  输入: 38
# 输出: 2 
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
#  
# 
#  进阶: 
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？ 
#  Related Topics 数学 数论 模拟 
#  👍 378 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 方法1：
        # if num < 10:
        #     return num
        # result = 0
        # while num >= 10:
        #     result = 0
        #     while num > 0:
        #         digit = num % 10
        #         num = num // 10
        #         result += digit
        #     num = result
        # return result

        # 方法2：O(1)
        if num % 9 == 0 and num > 0:
            return 9
        return num % 9
# leetcode submit region end(Prohibit modification and deletion)
