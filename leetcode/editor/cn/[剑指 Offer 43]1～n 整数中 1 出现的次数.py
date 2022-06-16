"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 

 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 

 

 示例 1： 

 
输入：n = 12
输出：5
 

 示例 2： 

 
输入：n = 13
输出：6 

 

 限制： 

 
 1 <= n < 2^31 
 

 注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/ 
 Related Topics 递归 数学 动态规划 👍 340 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        # 参考 https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/ji-jian-jie-fa-by-harrisliao/
        # 找规律
        a, b, one_count = 1, 10, 0
        while n >= a:
            x, y = divmod(n, b)

            if y >= a * 2:
                one_count += (x + 1) * a
            elif y >= a:
                one_count += y + 1 + (x - 1) * a
            else:
                one_count += x * a

            a, b = b, b * 10

        return one_count

# leetcode submit region end(Prohibit modification and deletion)
