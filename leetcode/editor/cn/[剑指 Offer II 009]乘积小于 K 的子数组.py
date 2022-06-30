"""
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。 

 

 示例 1: 

 
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
 

 示例 2: 

 
输入: nums = [1,2,3], k = 0
输出: 0 

 

 提示: 

 
 1 <= nums.length <= 3 * 10⁴ 
 1 <= nums[i] <= 1000 
 0 <= k <= 10⁶ 
 

 

 注意：本题与主站 713 题相同：https://leetcode-cn.com/problems/subarray-product-less-than-k/
 
 Related Topics 数组 滑动窗口 👍 83 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 超时
        # new_nums = [1]
        # for i in nums:
        #     new_nums.append(new_nums[-1]*i)
        # res = 0
        # for i in range(len(new_nums)-1):
        #     for j in range(i+1, len(new_nums)):
        #         if new_nums[j] // new_nums[i] < k:
        #             res += 1
        #         else:
        #             break
        # return res

        left, right = 0, 0
        res = 0
        cur_prob = 1
        while right < len(nums):
            cur_prob *= nums[right]
            while cur_prob >= k and left <= right:
                cur_prob //= nums[left]
                left += 1
            if cur_prob < k:
                res += right - left + 1  # 这里的递增，要理解为什么窗口每增大一位，就多right-left+1个res
            right += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
