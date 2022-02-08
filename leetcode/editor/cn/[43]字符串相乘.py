# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  
# 输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 和 num2 只能由数字组成。 
#  num1 和 num2 都不包含任何前导零，除了数字0本身。 
#  
#  Related Topics 数学 字符串 模拟 
#  👍 828 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tmp_out = []
        for i in range(len(num2)-1, -1, -1):
            tmp_out.append(self.mul(num1, num2[i]))
        res = 0
        for i, num in enumerate(tmp_out):
            res += num * (10**i)
        return str(res)

    def mul(self, num1, a):
        carry = 0
        res = []
        for i in range(len(num1)-1, -1, -1):
            out = int(num1[i]) * int(a) + carry
            left = out % 10
            carry = out // 10
            res.append(str(left))
            if i == 0 and carry != 0:
                res.append(str(carry))
        return int("".join(res[::-1]))
# leetcode submit region end(Prohibit modification and deletion)

