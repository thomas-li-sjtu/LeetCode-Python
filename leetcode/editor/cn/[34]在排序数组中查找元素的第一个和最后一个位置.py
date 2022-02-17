# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  nums 是一个非递减数组 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 二分查找 
#  👍 1454 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right, length = 0, len(nums)-1, len(nums)-1
        mid = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break
        print(mid)
        if mid == -1 or left > right:
            return [-1, -1]

        mid_left, mid_right = mid, mid
        while mid_left >= 0 and nums[mid_left] == target:
            if nums[mid_left] == target:
                mid_left -= 1
        while mid_right <= length and nums[mid_right] == target:
            if nums[mid_right] == target:
                mid_right += 1
        return [mid_left+1, mid_right-1]
# leetcode submit region end(Prohibit modification and deletion)
