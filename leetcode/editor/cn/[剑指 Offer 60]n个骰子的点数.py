"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。 

 

 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。 

 

 示例 1: 

 输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
 

 示例 2: 

 输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.0
5556,0.02778] 

 

 限制： 

 1 <= n <= 11 
 Related Topics 数学 动态规划 概率与统计 👍 435 👎 0

"""
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0 for _ in range(6*n)] for _ in range(n)]
        for i in range(6):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6*(i+1)):  # 本行[0，i-1]频数为0
                dp[i][j] = dp[i-1][j-6] + dp[i-1][j-5] + dp[i-1][j-4] + dp[i-1][j-3] + dp[i-1][j-2] + dp[i-1][j-1]
        total = sum(dp[-1])
        return [i/total for i in dp[-1] if i > 0]
# leetcode submit region end(Prohibit modification and deletion)
