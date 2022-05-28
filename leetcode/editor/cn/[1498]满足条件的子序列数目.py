"""
给你一个整数数组 nums 和一个整数 target 。 

 请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。 

 由于答案可能很大，请将结果对 10⁹ + 7 取余后返回。 

 

 示例 1： 

 
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
 

 示例 2： 

 
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6] 

 示例 3： 

 
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 1 <= nums[i] <= 10⁶ 
 1 <= target <= 10⁶ 
 
 Related Topics 数组 双指针 二分查找 排序 👍 88 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = int(10 ** 9 + 7)
        ret = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:  # 从右边开始减，直到找到合适的序列，更新l以后，r也要更新
                right -= 1
            else:
                ret = (ret + (1 << (right - left))) % mod  # 计算包含nums[l]的所有子集个数，这样l+1后，之后计算的子集里面肯定没有之前的nums[l]，这样就不会重复计算
                left += 1
        return ret
# leetcode submit region end(Prohibit modification and deletion)
