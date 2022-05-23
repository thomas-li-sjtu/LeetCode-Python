"""
元素的 频数 是该元素在一个数组中出现的次数。 

 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。 

 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。 

 

 示例 1： 

 
输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。 

 示例 2： 

 
输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
 

 示例 3： 

 
输入：nums = [3,9,6], k = 2
输出：1
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 1 <= nums[i] <= 10⁵ 
 1 <= k <= 10⁵ 
 
 Related Topics 数组 二分查找 前缀和 滑动窗口 👍 220 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # # 滑动窗口模板
        # left, right = 0, (0 or 1)
        # ret = total = 0
        # while right < len(nums):
        #     更新total值
        #     while 窗口内数据不满足要求
        #         1.更新total值
        #         2.收缩左边界
        #     更新ret最大值
        # 返回 ret

        # 每次右移一位，需要增加(right - left) * (nums[right] - nums[right - 1])这么多数字。
        # 那如果pre_sum不够了，需要收缩左边界呢？只用nums[right] - nums[left]
        # 我们使用一个滑动窗口模板，默认窗口拉伸，当pre_sum > k时，收缩左边界。直至满足条件，然后每次计算最大窗口距离
        nums.sort()
        left, right, pre_sum, ret = 0, 1, 0, 1
        while right < len(nums):
            pre_sum += (right - left) * (nums[right] - nums[right - 1])
            while pre_sum > k:
                pre_sum -= nums[right] - nums[left]
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        return ret
# leetcode submit region end(Prohibit modification and deletion)
