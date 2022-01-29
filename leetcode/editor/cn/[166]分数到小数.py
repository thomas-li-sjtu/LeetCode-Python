# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。 
# 
#  如果小数部分为循环小数，则将循环的部分括在括号内。 
# 
#  如果存在多个答案，只需返回 任意一个 。 
# 
#  对于所有给定的输入，保证 答案字符串的长度小于 104 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numerator = 1, denominator = 2
# 输出："0.5"
#  
# 
#  示例 2： 
# 
#  
# 输入：numerator = 2, denominator = 1
# 输出："2"
#  
# 
#  示例 3： 
# 
#  
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"
#  
# 
#  示例 4： 
# 
#  
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"
#  
# 
#  示例 5： 
# 
#  
# 输入：numerator = 1, denominator = 5
# 输出："0.2"
#  
# 
#  
# 
#  提示： 
# 
#  
#  -231 <= numerator, denominator <= 231 - 1 
#  denominator != 0 
#  
#  Related Topics 哈希表 数学 字符串 
#  👍 356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        res = []
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)  # 整数部分
        res.append(str(a))
        if b == 0:
            return "".join(res)
        # 小数部分
        res.append(".")
        dict_loc = {b: len(res)}
        while b != 0:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in dict_loc:  # 出现循环
                res.insert(dict_loc[b], "(")
                res.append(")")
                break
            dict_loc[b] = len(res)
        return "".join(res)
# leetcode submit region end(Prohibit modification and deletion)
