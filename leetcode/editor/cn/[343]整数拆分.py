"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。 

 返回 你可以获得的最大乘积 。 

 

 示例 1: 

 
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。 

 示例 2: 

 
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 

 

 提示: 

 
 2 <= n <= 58 
 
 Related Topics 数学 动态规划 👍 785 👎 0

"""
import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        # 当所有拆分出的数字相等时，乘积最大，最优拆分数字为3
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

# leetcode submit region end(Prohibit modification and deletion)
