"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等
。 

 请写一个函数，求任意第n位对应的数字。 

 

 示例 1： 

 输入：n = 3
输出：3
 

 示例 2： 

 输入：n = 11
输出：0 

 

 限制： 

 
 0 <= n < 2^31 
 

 注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/ 
 Related Topics 数学 二分查找 👍 258 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 将每个数字字符宽度补齐到当前宽度i，此时k就代表了第k个补全数字
        # 000 001 002 003 ...
        i = 1
        while i * (10 ** i) < n:
            n += 10 ** i
            i += 1
        return int(str(n // i)[n % i])
# leetcode submit region end(Prohibit modification and deletion)
