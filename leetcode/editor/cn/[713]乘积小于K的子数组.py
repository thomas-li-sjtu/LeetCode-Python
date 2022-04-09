"""
给定一个正整数数组 nums和整数 k 。 

 请找出该数组内乘积小于 k 的连续的子数组的个数。 

 

 示例 1: 

 
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
 

 示例 2: 

 
输入: nums = [1,2,3], k = 0
输出: 0 

 

 提示: 

 
 1 <= nums.length <= 3 * 10⁴ 
 1 <= nums[i] <= 1000 
 0 <= k <= 10⁶ 
 
 Related Topics 数组 滑动窗口 👍 384 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # # 前缀积，超时
        # prod = [1]
        # for i in range(len(nums)):
        #     prod.append(prod[-1]*nums[i])
        # # print(prod)
        # count = 0
        # for i in range(1, len(prod)):
        #     for j in range(0, i):
        #         if prod[i] // prod[j] < k:
        #             count += 1
        # return count

        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
