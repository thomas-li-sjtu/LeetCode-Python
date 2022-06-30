"""
给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。 

 

 示例 1： 

 
输入:nums = [1,1,1], k = 2
输出: 2
解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
 

 示例 2： 

 
输入:nums = [1,2,3], k = 3
输出: 2
 

 

 提示: 

 
 1 <= nums.length <= 2 * 10⁴ 
 -1000 <= nums[i] <= 1000 
 
 -10⁷ <= k <= 10⁷ 
 
 

 

 注意：本题与主站 560 题相同： https://leetcode-cn.com/problems/subarray-sum-equals-k/ 
 Related Topics 数组 哈希表 前缀和 👍 79 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        counts = 0
        dic = {}

        for num in nums:
            total += num
            if total == k:
                counts += 1
            if total - k in dic:
                counts += dic[total - k]
            dic[total] = dic.get(total, 0) + 1
        return counts
# leetcode submit region end(Prohibit modification and deletion)
