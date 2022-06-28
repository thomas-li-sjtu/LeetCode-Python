"""
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。 

 输入为 非空 字符串且只包含数字 1 和 0。 

 

 示例 1: 

 
输入: a = "11", b = "10"
输出: "101" 

 示例 2: 

 
输入: a = "1010", b = "1011"
输出: "10101" 

 

 提示： 

 
 每个字符串仅由字符 '0' 或 '1' 组成。 
 1 <= a.length, b.length <= 10^4 
 字符串如果不是 "0" ，就都不含前导零。 
 

 

 注意：本题与主站 67 题相同：https://leetcode-cn.com/problems/add-binary/ 
 Related Topics 位运算 数学 字符串 模拟 👍 39 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        min_len = min(len(a), len(b))
        a = [int(i) for i in a][::-1]
        b = [int(i) for i in b][::-1]
        res = []
        carry = 0
        for i in range(min_len):
            res.append(a[i] ^ b[i] ^ carry)
            if a[i] + b[i] + carry >= 2:
                carry = 1
            else:
                carry = 0
        if len(a) == len(b):
            if carry != 0:
                res.append(carry)
        elif len(a) > len(b):
            for i in range(min_len, len(a)):
                res.append(a[i] ^ carry)
                if a[i] + carry >= 2:
                    carry = 1
                else:
                    carry = 0
            if carry != 0:
                res.append(carry)
        else:
            for i in range(min_len, len(b)):
                res.append(b[i] ^ carry)
                if b[i] + carry >= 2:
                    carry = 1
                else:
                    carry = 0
            if carry != 0:
                res.append(carry)
        return "".join([str(i) for i in res[::-1]])

# leetcode submit region end(Prohibit modification and deletion)
