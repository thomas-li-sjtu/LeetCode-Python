# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。 
# 
#  请你找出并返回只出现一次的那个数。 
# 
#  你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,2,3,3,4,4,8,8]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: nums =  [3,3,7,7,10,11,11]
# 输出: 10
#  
# 
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 105 
#  0 <= nums[i] <= 105 
#  
#  Related Topics 数组 二分查找 
#  👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 在进行中间元素判断时可发现如果 mid 为奇数且前半部分无单一元素的时有array[mid] = array[mid-1]  (数组从0开始计数），
        # 因此不满足这种情况就表明单一元素在前半部分，可以令 high = mid -1; 否则表明单一元素在后半部分，可以令 low= mid + 1
        # 反之亦然

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    right = mid
                elif nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                elif nums[mid] == nums[mid+1]:
                    right = mid
                else:
                    return nums[mid]

        return nums[left]

# leetcode submit region end(Prohibit modification and deletion)
