# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。 
# 
#  如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true
#  ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组 
# 
#  示例 3： 
# 
#  
# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5 * 105 
#  -231 <= nums[i] <= 231 - 1 
#  
# 
#  
# 
#  进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？ 
#  Related Topics 贪心 数组 
#  👍 548 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        left_min = [0]*len(nums)
        right_max = [0]*len(nums)
        min_num = nums[0]
        for i in range(1, len(nums)):
            if min_num < nums[i]:
                left_min[i] = min_num
            else:
                left_min[i] = min_num
                min_num = nums[i]

        max_num = nums[-1]
        for i in range(len(nums)-2, 0, -1):
            if max_num > nums[i]:
                right_max[i] = max_num
            else:
                right_max[i] = max_num
                max_num = nums[i]

        for i in range(1, len(nums)-1):
            if left_min[i] < nums[i] < right_max[i]:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
