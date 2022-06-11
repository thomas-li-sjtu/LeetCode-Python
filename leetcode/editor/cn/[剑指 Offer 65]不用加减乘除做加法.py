"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。 

 

 示例: 

 输入: a = 1, b = 1
输出: 2 

 

 提示： 

 
 a, b 均可能是负数或 0 
 结果不会溢出 32 位整数 
 
 Related Topics 位运算 数学 👍 321 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def add(self, a: int, b: int) -> int:
        # 亦或 相当于无进位的求和
        # 与 相当于求每位的进位数
        # 公式是：（a ^ b) ^ ((a & b) << 1)
        # 即：每次无进位求 + 每次得到的进位数
        # 需要不断重复这个过程直到进位数为0为止；
        x = 0xffffffff  # 将加数32位以上的数字全部置为0
        a, b = a & x, b & x
        while b != 0:
            a, b = a ^ b, (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)  # python中补码是符号位以上的高位全部为1，所以需要将32位以上的0全部取反
# leetcode submit region end(Prohibit modification and deletion)
