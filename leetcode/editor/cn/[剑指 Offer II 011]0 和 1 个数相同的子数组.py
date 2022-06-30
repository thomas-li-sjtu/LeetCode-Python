"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 

 

 示例 1： 

 
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 

 示例 2： 

 
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 nums[i] 不是 0 就是 1 
 

 

 注意：本题与主站 525 题相同： https://leetcode-cn.com/problems/contiguous-array/ 
 Related Topics 数组 哈希表 前缀和 👍 74 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -1 if nums[i] == 0 else 1
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)

        sum_dict = {}
        res = 0

        for i in range(len(pre_sum)):
            if sum_dict.get(pre_sum[i]) is not None:
                res = max(res, i - sum_dict[pre_sum[i]])
            else:
                sum_dict[pre_sum[i]] = i
        return res
# leetcode submit region end(Prohibit modification and deletion)
