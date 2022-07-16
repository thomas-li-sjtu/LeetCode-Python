"""
给定一个正整数数组 nums 和一个整数 target 。 

 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 

 
 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
 

 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 

 

 示例 1： 

 
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
 

 示例 2： 

 
输入：nums = [1], target = 1
输出：1
 

 

 提示： 

 
 1 <= nums.length <= 20 
 0 <= nums[i] <= 1000 
 0 <= sum(nums[i]) <= 1000 
 -1000 <= target <= 1000 
 

 

 注意：本题与主站 494 题相同： https://leetcode-cn.com/problems/target-sum/ 
 Related Topics 数组 动态规划 回溯 👍 24 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 全局回溯，超时
        # def back(start, end, cur_val, length):
        #     if length == len(nums) and cur_val == target:
        #         self.res += 1
        #     else:
        #         for i in range(start, end):
        #             cur_val += nums[i]
        #             back(i+1, end, cur_val, length+1)
        #             cur_val -= nums[i]
        #
        #             cur_val -= nums[i]
        #             back(i+1, end, cur_val, length+1)
        #             cur_val += nums[i]
        # self.res = 0
        # back(0, len(nums), 0, 0)
        # return self.res

        """ pos + neg = total  """
        """ pos - neg = target """
        total = sum(nums)
        if abs(target) > total:  # target可能为负
            return 0
        if (total + target) % 2 == 1:  # 不能被2整除【对应于pos不是整数】
            return 0

        """【0/1背包】：从nums中选出数字组成pos或neg"""
        pos = (total + target) // 2
        neg = (total - target) // 2
        capcity = min(pos, neg)  # 取pos和neg中的较小者，以使得dp空间最小
        n = len(nums)

        # 初始化
        dp = [[0] * (capcity + 1) for _ in range(n + 1)]
        # dp[i][j]: 从前i个元素中选出若干个其和为j的方案数
        dp[0][0] = 1  # 其他 dp[0][j]均为0

        # 状态更新
        for i in range(1, n + 1):
            for j in range(capcity + 1):
                if j < nums[i - 1]:  # 容量有限，无法选择第i个数字nums[i-1]
                    dp[i][j] = dp[i - 1][j]
                else:  # 可选择第i个数字nums[i-1]，也可不选【两种方式之和】
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

        return dp[n][capcity]

# leetcode submit region end(Prohibit modification and deletion)
