"""
给你一个整数数组 nums 和一个整数 target 。 

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
 
 Related Topics 数组 动态规划 回溯 👍 1270 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # # 深度优先搜索 超时
        # stack = [(0, -1)]
        # length = len(nums)
        # counter = 0
        # while stack:
        #     cur_sum, index = stack.pop()
        #     if index != length-1:
        #         stack.append((cur_sum + nums[index+1], index+1))
        #         stack.append((cur_sum - nums[index+1], index+1))
        #     else:
        #         counter += 1 if cur_sum == target else 0
        # return counter

        # 深度优先搜索
        # d = {}
        #
        # def dfs(cur, i, d):
        #     if i < len(nums) and (cur, i) not in d:  # 搜索周围节点
        #         d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i], i + 1, d)
        #     return d.get((cur, i), int(cur == target))
        #
        # return dfs(0, 0, d)

        sumAll = sum(nums)
        target = abs(target)
        if target > sumAll or (target + sumAll) % 2:
            return 0
        new_target = (target + sumAll) // 2

        dp = [0] * (new_target + 1)
        dp[0] = 1

        for num in nums:
            for j in range(new_target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
