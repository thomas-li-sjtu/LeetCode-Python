# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
# 
#  例如： 
# 
#  
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：columnNumber = 1
# 输出："A"
#  
# 
#  示例 2： 
# 
#  
# 输入：columnNumber = 28
# 输出："AB"
#  
# 
#  示例 3： 
# 
#  
# 输入：columnNumber = 701
# 输出："ZY"
#  
# 
#  示例 4： 
# 
#  
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= columnNumber <= 231 - 1 
#  
#  Related Topics 数学 字符串 
#  👍 481 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # 1、题目中要求，对26取余的数值是从1开始的，并非从日常的0开始，所以当余数为0时，可当做26进行处理，因为26代表字母’Z’；
        # 2、由于取余的数值从1~26，那么下面对26取整的时候，要减去余数的值，否则将会不成功，比如52 = 1 * (26的1次方) + 26 *（26的0次方)，所以52对应Excel列为”AZ“：
        # （1）取余：余数为0：按照26处理，str字符串加入Z字符
        # （2）取整：columnNumber = columnNumber // 26 这时，columnNumber为2，but我们需要的字符是A而非B（因为52 = 1 * (26的1次方) + 26 *（26的0次方)）
        out = ''
        while columnNumber:
            temp = columnNumber % 26
            if temp == 0:  # 注意这里
                temp = 26
            out += chr(temp + 64)
            columnNumber -= temp  # 注意这里
            columnNumber //= 26
        return out[::-1]
# leetcode submit region end(Prohibit modification and deletion)
