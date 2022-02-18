# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。
#  
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,1,2]
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 104 
#  1 <= nums[i] <= 106 
#  
#  Related Topics 贪心 数组 数学 排序 
#  👍 162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, k = 0, 1, 2
        flag = 0
        nums = sorted(nums, reverse=True)
        for tmp in range(len(nums)-2):
            if nums[j] + nums[k] > nums[i]:
                flag = 1
                break
            else:
                i += 1
                j, k = i+1, i+2
        if flag:
            return nums[i] + nums[j] + nums[k]
        else:
            return 0
# leetcode submit region end(Prohibit modification and deletion)
