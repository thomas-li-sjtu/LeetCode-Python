# 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。 
# 
#  你可以假设所有输入数组都可以得到满足题目要求的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,1,1,6,4]
# 输出：[1,6,1,5,1,4]
# 解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,3,2,2,3,1]
# 输出：[2,3,1,3,1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5 * 104 
#  0 <= nums[i] <= 5000 
#  题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果 
#  
# 
#  
# 
#  进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？ 
#  Related Topics 数组 分治 快速选择 排序 
#  👍 328 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 寻找中位数, 然后将中位数放到中间，左边数字小于它，右边数字大于它
        # 依据中位数分割数组，反序，穿插排列即可
        import copy
        n = len(nums)
        if n <= 1:
            return nums
        k = (n + 1) // 2 - 1
        mid_value = self.partition(nums, k, 0, n - 1)
        self.three_way_partition(nums, mid_value)
        nums0 = copy.deepcopy(nums)
        for k in range(n):
            nums[k] = nums0[(n + 1) // 2 - 1 - k // 2] if (not k % 2) else nums0[(n - 1) - k // 2]

    def partition(self, nums, k, start, end):
        key = nums[start]
        left, right = start, end
        # 循环中的不变量: left<right and nums[right]>=key and nums[left]<=key
        while left < right:
            while left < right and nums[right] >= key:
                right = right - 1
            if left < right: nums[left], nums[right] = nums[right], nums[left]
            while left < right and nums[left] <= key:
                left = left + 1
            if left < right: nums[left], nums[right] = nums[right], nums[left]

        if left == k:
            return nums[left]
        elif left > k:
            return self.partition(nums, k, start, left - 1)
        else:
            return self.partition(nums, k, left + 1, end)

    def three_way_partition(self, nums, value):
        n = len(nums)
        l, r = 0, n - 1
        i = 0
        # 不能让i越过r 否则如果nums[l]<=nums[r]<nums[i] 会在下一次中让右侧更大的数字被换到左侧
        while i <= r:
            if nums[i] < value:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] > value:  # 在这种情况下i不要移动 因为交换过来的数字nums[r]可能仍是>value
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
# leetcode submit region end(Prohibit modification and deletion)
