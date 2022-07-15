"""
给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。 

 

 示例 1： 

 
输入：nums = [1,5,11,5]
输出：true
解释：nums 可以分割成 [1, 5, 5] 和 [11] 。 

 示例 2： 

 
输入：nums = [1,2,3,5]
输出：false
解释：nums 不可以分为和相等的两部分
 

 

 

 提示： 

 
 1 <= nums.length <= 200 
 1 <= nums[i] <= 100 
 

 

 注意：本题与主站 416 题相同： https://leetcode-cn.com/problems/partition-equal-subset-sum/ 

 Related Topics 数学 字符串 模拟 👍 48 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        nums_sum //= 2
        dct = dict()
        for num in nums:
            for k in list(dct.keys()):
                dct[k + num] = 1
            dct[num] = 1
            if nums_sum in dct:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
