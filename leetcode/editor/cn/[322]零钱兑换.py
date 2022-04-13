"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 

 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 

 你可以认为每种硬币的数量是无限的。 

 

 示例 1： 

 
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1 

 示例 2： 

 
输入：coins = [2], amount = 3
输出：-1 

 示例 3： 

 
输入：coins = [1], amount = 0
输出：0
 

 

 提示： 

 
 1 <= coins.length <= 12 
 1 <= coins[i] <= 2³¹ - 1 
 0 <= amount <= 10⁴ 
 
 Related Topics 广度优先搜索 数组 动态规划 👍 1873 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # 超时
        # res = []
        # paths = []
        # coins.sort()
        # target = amount
        #
        # def combine(start, target):
        #     if target == 0:
        #         res.append(len(paths))
        #     else:
        #         for i in range(start, len(coins)):
        #             if target - coins[i] >= 0:
        #                 paths.append(coins[i])
        #                 combine(i, target-coins[i])
        #                 paths.pop()
        # combine(0, target)
        #
        # return min(res) if res else -1

        # dp[j]代表含义：填满容量为j的背包最少需要多少硬币
        # 初始化dp数组：因为硬币的数量一定不会超过amount，而amount <= 10^4，因此初始化数组值为10001；dp[0] = 0
        # 转移方程：dp[j] = min(dp[j], dp[j - coin] + 1)——填满容量j最少需要的硬币 = min(之前填满容量j最少需要的硬币, 填满容量j-coin需要的硬币 + 1个当前硬币）
        # 返回dp[amount]，如果dp[amount]的值为10001没有变过，说明找不到硬币组合，返回-1

        dp = [0] + [10001] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[-1] if dp[-1] != 10001 else -1


# leetcode submit region end(Prohibit modification and deletion)

