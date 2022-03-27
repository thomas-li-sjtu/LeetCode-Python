"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 

 测试用例的答案是一个 32-位 整数。 

 子数组 是数组的连续子序列。 

 

 示例 1: 

 
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
 

 示例 2: 

 
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 

 

 提示: 

 
 1 <= nums.length <= 2 * 10⁴ 
 -10 <= nums[i] <= 10 
 nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数 
 
 Related Topics 数组 动态规划 👍 1575 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [nums[0]]
        dp_min = [nums[0]]
        for i in range(1, len(nums)):
            dp_max.append(max(nums[i], nums[i]*dp_max[i-1], nums[i]*dp_min[i-1]))
            dp_min.append(min(nums[i], nums[i]*dp_min[i-1], nums[i]*dp_max[i-1]))
        return max(dp_max)
# leetcode submit region end(Prohibit modification and deletion)
